# Implementation Plan

## Overview
Extend the proven ECA pipeline from `research/raw/Stage 1/Archive` to `Rules and Regulations/Commander Deck/Archive` so governance history is compressed, encrypted at rest, excluded from ingestion, but fully interrogable via `restore_archive.py --list` and full restore.

Silent investigation findings: (1) Stage 1 Wave 1 archive is healthy — 13/13 files, VERIFIED_OK, 482433 to 150269 bytes (3.21x), decrypt verified via `--list`. (2) Current ECA method (tar.gz level 9 + AES-256-GCM + PBKDF2 600k + ECA1 container + JSON manifest + verify-before-delete) is correct — keep it, only generalize CLI. (3) Commander Deck Archive is 4 plaintext .md files (~30KB total: Plan 2.md 631B, Plan First Citation Intelligence Database.md 9772B, Solutions1.md 19406B, state change 001.md 970B) with no encryption. (4) Duplicated Protocols trees (root `Protocols/` vs `Rules and Regulations/Protocols/`) cause `check_paths` fragility (22 violations when one copy missing).

## Types
- `ECA-v1 Container` (unchanged, `src/archive_core.py:23-29`): `[0:4] MAGIC ECA1 | [4:20] salt 16B | [20:32] nonce 12B | [32:48] GCM tag 16B | [48:] ciphertext`.
- `Manifest JSON` (unchanged shape from `build_manifest_data`): `{format, created_utc, archive_file, source_directory, file_count, total_uncompressed_bytes, total_compressed_bytes, compression_ratio, verification_status: VERIFIED_OK, cipher, kdf, files: [{path, size_bytes, sha256}]}`. New files use prefix `commander_deck_archive_<timestamp>`.
- `CLI ArchiveParams`: `{source_dir, dest_dir, prefix, dry_run, keep_originals, passphrase, passphrase_env}`. `prefix` defaults to `wave_1_archive` for back-compat.
- `InterrogationResult` (existing): `--list` gives in-memory `{name, size, sha256[:12]}` table without disk writes.

## Files (part 1 — new)
- `implementation_plan.md` (this file; move to `Rules and Regulations/Commander Deck/Plans/` on approval).
- No new runtime files if Option A chosen. Optional thin wrapper `scripts/archive_commander_deck.py` delegating to `run_archive` with Commander Deck defaults.
## Files (part 2 - modify)
- `scripts/archive_stage1.py`: add `--prefix` arg (default `wave_1_archive`), always skip `*_manifest.json` + `*.tar.gz.enc`.
- `scripts/restore_archive.py`: keep crypto; update `--dest` help for Commander Deck; optional `--json` for `--list`.
- `Rules and Regulations/Protocols/Encryption-Compression-Archiving.md`: parameterize Wave-1 paths; add 4.10 Commander Deck profile; add 5.3 interrogation-without-restore.
- `Protocols/` vs `Rules and Regulations/Protocols/`: canonicalize to one location (duplicate caused 22 check_paths failures).
- `src/prompt_templates/**`: fix bare `Protocols/...` refs to canonical path. `.gitignore`: keep ignoring `*.tar.gz.enc`, allow manifests. `AGENTS.md`: add Commander Deck examples.

## Files (part 3 - delete/config)
- Delete: none by hand (archiver deletes only after verified roundtrip). Config: reuse the `ARCHIVE_PASSPHRASE` environment variable (`.env` holds no secrets).

## Functions
- New: none (optional `scripts/archive_commander_deck.py:main()` wrapper).
- Modified `run_archive()`: add `prefix` param, skip enc/manifest, return tuple for testability.
- `src/archive_core.py`: NO changes (already generic).
## Classes
- None new/modified/removed. Reuse ArchiveError/AuthenticationError/IntegrityError.

## Dependencies
- No new packages. Alternatives rejected: git-annex/DVC (overkill), zip+ZipCrypto (forbidden unauthenticated), age+zstd (breaks ECA1 standard + 11 tests), DuckDB BLOB (violates DB topology rule). Keep ECA1.

## Testing
- Stay green: test_archive_roundtrip.py (11 tests) + full suite 67 passed.
- New tests: dry_run_creates_nothing, roundtrip_with_prefix, enc-manifest-excluded, enc-excluded-from-ingestion, list-without-extract.

## Implementation Order
1. Canonicalize Protocols path, confirm 67/67 green. 2. Generalize archive_stage1.py. 3. Dry-run Commander Deck (expect 4 files ~30KB). 4. Real archive keep-originals, verify list. 5. Exclusion check DB counts unchanged. 6. Verified delete pass. 7. Update docs + final pytest.
