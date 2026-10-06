---
name: eca-archiving
description: "Archives research raw files and Commander Deck governance history into ECA (Encrypted Compression-Archive) format — lossless gzip tarball + AES-256-GCM authenticated encryption + PBKDF2-HMAC-SHA256 (600k iterations), with zero-trust roundtrip verification before any source file is deleted."
version: 1.0.0
---

# Encryption-Compression-Archiving (ECA)

Archives research raw materials in `research/raw/Stage 1/` and governance history in `Rules and Regulations/Commander Deck/Archive` into ECA format (`.tar.gz.enc`). Distilled from `Rules and Regulations/Protocols/Encryption-Compression-Archiving.md`.

## When to use this skill

- Archiving completed Stage 1 research briefs into `research/raw/Stage 1/Archive/`
- Archiving Commander Deck governance history in place
- Restoring files from an existing `.tar.gz.enc` archive
- Interrogating (listing) an archive without writing files to disk
- Asked to "archive Wave 1" or "compress and encrypt research raw"

## Prerequisites

- Source directory exists and contains `.md` files (e.g., `research/raw/Stage 1/Wave 1/`)
- Python venv with dependencies installed (`duckdb, pandas, cryptography, ...`)
- Archive passphrase ready: set `ARCHIVE_PASSPHRASE` env var, or use the secure interactive prompt
- `.tar.gz.enc` files are gitignored derived artifacts; their `*_manifest.json` are the committed audit trail

## Cryptographic Specification

| Component | Value |
|---|---|
| Compression | `tar.gz` (gzip, level 9), assembled **in memory** |
| Cipher | AES-256-GCM (AEAD — authenticated encryption; detects tampering) |
| Key Derivation | PBKDF2-HMAC-SHA256, 600,000 iterations |
| Salt | 16 bytes cryptographically random per archive |
| Nonce (IV) | 12 bytes cryptographically random per archive |
| Auth Tag | 16 bytes |
| Magic Header | `b"ECA1"` (4 bytes, "Encryption-Compression-Archive v1") |
| Container Layout | `[ECA1][16B salt][12B nonce][16B tag][ciphertext]` — 48-byte header |

Any alteration to the magic, salt, nonce, tag, or ciphertext causes authentication to fail **before** data is written to disk.

## The Process

### Step 1: File Discovery & Inventory
Locate all `.md` files in the source directory. The archiver never re-archives `*.tar.gz.enc` or `*_manifest.json`. Abort if zero readable files found.

### Step 2: Pre-Archive Checksums
Read each file and compute its SHA-256. Record relative path, byte size, and mtime in an in-memory inventory.

### Step 3: In-Memory Compression
Assemble files into a POSIX tar archive and gzip-compress to level 9 **in memory** — no intermediate unencrypted files on disk.

### Step 4: Key Derivation
Acquire the passphrase via the `ARCHIVE_PASSPHRASE` env var (or `.env`), or a secure interactive prompt with hidden input and confirmation. Generate a 16-byte random salt. Derive the 32-byte (256-bit) AES key.

### Step 5: AES-256-GCM Encryption
Generate a 12-byte random nonce. Encrypt the tarball and extract the 16-byte auth tag.

### Step 6: Atomic Container Emission
Assemble the 48-byte header + ciphertext and write atomically to:
- **Research:** `research/raw/Stage 1/Archive/wave_1_archive_<timestamp>.tar.gz.enc`
- **Commander Deck:** `Rules and Regulations/Commander Deck/Archive/commander_deck_archive_<timestamp>.tar.gz.enc`

### Step 7: Zero-Trust Roundtrip Verification (MANDATORY before any deletion)
Read the written container back from disk, decrypt, decompress in memory, recompute SHA-256 of every file, and compare against the pre-archive inventory. If anything mismatches or the GCM tag fails:
- The archive is **deleted from disk**
- **Original source files are untouched**
- A diagnostic alert is emitted

### Step 8: Manifest & Audit Log
Write `<archive>_manifest.json` (unencrypted audit trail, committed to git):
- Format (`ECA-v1`), creation timestamp, archive filename
- Source directory, file count, uncompressed/compressed sizes, compression ratio
- `verification_status: "VERIFIED_OK"`
- Per-file entries: path, size_bytes, sha256

### Step 9: Source Cleanup (post-verify only)
Remove the verified originals from the source directory, leaving it present and clean. Use `--keep-originals` to skip this.

### Step 10: Commander Deck Profile (in-place archiving)
Source **and** destination are `Rules and Regulations/Commander Deck/Archive/`. Prefix `commander_deck_archive`. Same cipher, KDF, manifest schema, and zero-trust verify-before-delete. `.tar.gz.enc` files are gitignored; `*_manifest.json` files are the committed audit trail.

## CLI Commands

### Dry-run — always first (per `AGENTS.md`)
```powershell
.venv\Scripts\python.exe scripts/archive_stage1.py --source "research/raw/Stage 1/Wave 1" --dest "research/raw/Stage 1/Archive" --prefix wave_1_archive --dry-run
```

### Archive Wave 1 research briefs
```powershell
.venv\Scripts\python.exe scripts/archive_stage1.py --source "research/raw/Stage 1/Wave 1" --dest "research/raw/Stage 1/Archive" --prefix wave_1_archive
```

### Archive Commander Deck governance history (in place)
```powershell
.venv\Scripts\python.exe scripts/archive_stage1.py --source "Rules and Regulations/Commander Deck/Archive" --dest "Rules and Regulations/Commander Deck/Archive" --prefix commander_deck_archive --dry-run
.venv\Scripts\python.exe scripts/archive_stage1.py --source "Rules and Regulations/Commander Deck/Archive" --dest "Rules and Regulations/Commander Deck/Archive" --prefix commander_deck_archive
```

### Restoration — list without extracting
```powershell
.venv\Scripts\python.exe scripts/restore_archive.py --archive "research/raw/Stage 1/Archive/wave_1_archive_<timestamp>.tar.gz.enc" --list
```

### Restoration — full restore
```powershell
.venv\Scripts\python.exe scripts/restore_archive.py --archive "research/raw/Stage 1/Archive/wave_1_archive_<timestamp>.tar.gz.enc" --dest "research/raw/Stage 1/Wave 1"
```

## Quality Gates

- [ ] **Dry run first** — never archive live without `--dry-run` (per `AGENTS.md` maintenance note)
- [ ] **Verified before deletion** — `VERIFIED_OK` present in manifest; source files untouched on failure
- [ ] **Lossless** — roundtrip SHA-256 of every file matches the pre-archive inventory exactly
- [ ] **Authenticated only** — AES-256-GCM used; no CBC/ZipCrypto
- [ ] **Manifest integrity** — `_manifest.json` written to the archive destination and committed to git
- [ ] **Secrets hygiene** — passphrase never committed; use `ARCHIVE_PASSPHRASE` env var

## Error Handling & Recovery

| Failure Mode | Behavior | Recovery |
|---|---|---|
| Wrong passphrase during verify | Archive rejected; source files untouched | Re-enter passphrase via prompt/env var |
| Checksum mismatch during verify | Archive deleted; originals untouched | Diagnostic alert; inspect disk/memory |
| Container corrupted on disk | Restore aborts with `AuthenticationError` | Use `*_manifest.json` to identify damage; restore from backup |
| Tampered ciphertext | GCM tag verification fails immediately; no decompression | Tamper alert logged; data not written to disk |

## Non-Negotiable Rules

1. **Never delete or move originals based on an exit code alone** — a roundtrip SHA-256 comparison against every file must pass first.
2. **Use authenticated encryption only** — AES-256-GCM with 600k PBKDF2 iterations; hardcoded keys and static salts are forbidden.
3. **No intermediate unencrypted temporary files** — the tarball is assembled and compressed in memory.
4. **Always `--dry-run` first** — per `AGENTS.md` maintenance notes.
5. **Never commit passphrases, `.key` files, or decrypted secrets to git** — `*.tar.gz.enc` are derived artifacts; `*_manifest.json` is the committed audit trail.
6. **Keep `Wave 1/` and the archive directories present** — only file *contents* are removed/archived; directories stay clean and ready.

## Output

After a successful archive:
- `<prefix>_YYYYMMDD_HHMMSS.tar.gz.enc` — the encrypted, compressed container
- `<prefix>_YYYYMMDD_HHMMSS_manifest.json` — unencrypted audit manifest (committed to git)

After a successful restore:
- Original files recovered verbatim into `--dest`, with per-file SHA-256 extraction logs.

## References

- Protocol: `Rules and Regulations/Protocols/Encryption-Compression-Archiving.md`
- Core library: `src/archive_core.py` (`encrypt_payload`, `decrypt_container`, `verify_archive_data`, `build_manifest_data`)
- CLI archiver: `scripts/archive_stage1.py` (`--dry-run`, `--keep-originals`, `--prefix`, `ARCHIVE_PASSPHRASE`)
- CLI restorer: `scripts/restore_archive.py` (`--list`, `--overwrite`)
- Repository rules: `AGENTS.md` (maintenance: dry-run first; keep `SMARTHOME_DB` consistent)
