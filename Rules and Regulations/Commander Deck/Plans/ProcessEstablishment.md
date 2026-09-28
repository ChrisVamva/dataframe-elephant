---
modified: 2026-09-28T00:00:00+03:00
status: active
scope: Rules and Regulations/Commander Deck/Archive
method: ECA-v1 (same as Stage 1 Wave 1)
---

# Process Establishment — Commander Deck Archive (ECA)

## 1. Decision

Apply the proven Encryption-Compression-Archiving (ECA) pipeline —
currently used for `research/raw/Stage 1/Archive` — to
`Rules and Regulations/Commander Deck/Archive`.

Chosen scope (user-confirmed 2026-09-28):
**Archive only the 4 files in `Commander Deck/Archive`, verified delete.**
Originals are removed only after a 100% SHA-256 verified roundtrip,
identical to the Stage 1 process.

## 2. Data accessibility (verified 2026-09-28)

| Location | Content | Status |
| --- | --- | --- |
| `research/raw/Stage 1/Archive/wave_1_archive_20260927_192048.tar.gz.enc` | 13 files, 482,433 → 150,269 bytes (3.21x), manifest `VERIFIED_OK` | Decrypt verified via `restore_archive.py --list` |
| `research/raw/Stage 1/Archive/wave_1_archive_20260927_192048_manifest.json` | 13 entries with SHA-256 | Readable, committed audit trail |
| `Rules and Regulations/Commander Deck/Archive/` | 4 plaintext `.md` (~30 KB: `Plan 2.md` 631 B, `Plan First Citation Intelligence Database.md` 9,772 B, `Solutions1.md` 19,406 B, `state change 001.md` 970 B) | To be archived by this process |

## 3. Is ECA the best method? Yes — keep it.

Kept: `tar.gz` (level 9, lossless) + AES-256-GCM (authenticated) +
PBKDF2-HMAC-SHA256 (600,000 iterations, 16 B salt) + `ECA1` container
(MAGIC 4 B + salt 16 B + nonce 12 B + tag 16 B + ciphertext) +
unencrypted JSON manifest + zero-trust roundtrip-verify-before-delete
(`src/archive_core.py`, 11 roundtrip tests green).

Rejected: git-annex/DVC (overkill, weaker auth-encryption story);
plain zip + ZipCrypto (unauthenticated — forbidden by protocol §2.3);
age + zstd (breaks ECA1 standard, manifest tooling, `restore_archive.py`);
DuckDB BLOB table (couples cold storage to query engine, violates
`FromStagetoDatabases.md` topology rule).

## Verification (2026-09-28 run)
- Commander Deck: 4 files archived (30,779 to 11,558 bytes, 2.66x, VERIFIED_OK); originals removed only after the verified `--keep-originals` pass + `--list` confirmation; `Archive/` now holds only `.tar.gz.enc` (gitignored) + `_manifest.json` (committed audit trail).
- Ingestion exclusion proven: `citations.duckdb` rebuilt to 10 docs / 204 sources / 443 occurrences / 594 warnings — the +2 docs are `Stage 1/Citations/Citation.md` + `Report.md` (restored from Wave 1 archive work, not Commander Deck); zero Archive rows from either `.enc` (glob-proof) or plaintext (hook matcher is `research/raw/`-only).
- Bonus fix (pre-existing, found during exclusion check): full rebuild crashed with FK violation `ingestion_warning.run_id -> ingestion_run` because carried-forward warnings kept the OLD run_id. Fixed in `src/ingest_citations.py:_copy_unchanged_rows` + `src/stage2_import_core.py:_copy_unchanged_rows` by re-stamping carried warnings to the new run_id via `_make_warning`/`_warn`. Full suite: 68 passed.

## 4. Process (same as Stage 1, parameterized)

1. Dry-run first:
   `archive_stage1.py --source "Rules and Regulations/Commander Deck/Archive" --dest "Rules and Regulations/Commander Deck/Archive" --prefix commander_deck_archive --dry-run`
   (expects 4 files, ~30 KB, nothing written).
2. Real archive with `--keep-originals`; verify `--list` shows 4 files
   with matching SHA-256 and manifest `VERIFIED_OK`.
3. Exclusion check: rebuild both DuckDBs; counts must be unchanged
   (citations: 8 docs / 18 sources / 20 occurrences;
   stage 2: 7 docs / 22 entities / 29 decisions); `.enc` never matches
   ingestion `rglob("*.md")` so archives stay out of the process.
4. Verified delete pass (no `--keep-originals`; aborts + retains
   originals on any mismatch). `Archive/` ends with only
   `commander_deck_archive_<ts>.tar.gz.enc` + `_manifest.json`.

## 5. Interrogation in the future (data stays usable)

- List without extracting:
  `restore_archive.py --archive <file.tar.gz.enc> --list`
  (in-memory decrypt + decompress, name/size/sha table, zero disk writes).
- Audit via manifest (`*_manifest.json` stays committed, unencrypted).
- Full restore:
  `restore_archive.py --archive <file> --dest <dir> [--overwrite]`.
- Passphrase order unchanged: `--passphrase` → `$ARCHIVE_PASSPHRASE` →
  `.env` → interactive prompt. `.enc` files stay gitignored; manifests stay.

## 6. Code changes required

- `scripts/archive_stage1.py`: add `--prefix` (default `wave_1_archive`
  for back-compat); always skip `*_manifest.json` + `*.tar.gz.enc`.
- `scripts/restore_archive.py`: crypto unchanged; clarify `--dest` help
  for Commander Deck; optional `--json` for `--list`.
- `Rules and Regulations/Protocols/Encryption-Compression-Archiving.md`:
  parameterize Wave-1-only paths; add §4.10 Commander Deck profile +
  §5.3 interrogation-without-restore.
- Canonicalize duplicated `Protocols/` trees (root vs
  `Rules and Regulations/Protocols/`) — the duplication caused 22
  `check_paths` violations when out of sync; fix `prompts/**` refs after.
- `.gitignore`: keep ignoring `*.tar.gz.enc`, keep allowing manifests.
- `AGENTS.md`: add Commander Deck archive/restore examples.
- Tests: extend `src/tests/test_archive_roundtrip.py` (dry-run nothing,
  prefix roundtrip, enc/manifest exclusion, ingestion exclusion,
  list-without-extract). `src/archive_core.py`: no changes.
