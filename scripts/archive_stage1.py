"""CLI tool for Encryption-Compression-Archiving Stage 1 research files."""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add project root to sys.path so src imports work cleanly
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.archive_core import (  # noqa: E402
    ArchiveError,
    AuthenticationError,
    IntegrityError,
    build_manifest_data,
    compute_sha256,
    create_tar_gz,
    encrypt_payload,
    verify_archive_data,
)


def get_passphrase(args: argparse.Namespace) -> str:
    """Retrieve passphrase from flag, environment variable, .env file, or interactive prompt."""
    if args.passphrase:
        return args.passphrase

    env_val = os.environ.get(args.passphrase_env)
    if env_val:
        return env_val

    # Check for .env file in project root
    dotenv_path = PROJECT_ROOT / ".env"
    if dotenv_path.is_file():
        for line in dotenv_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith(f"{args.passphrase_env}="):
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                if val:
                    return val

    # Interactive prompt
    while True:
        p1 = getpass.getpass("Enter archive passphrase: ")
        if not p1:
            print("Passphrase cannot be empty. Please try again.", file=sys.stderr)
            continue
        p2 = getpass.getpass("Confirm archive passphrase: ")
        if p1 != p2:
            print("Passphrases do not match. Please try again.", file=sys.stderr)
            continue
        return p1


def run_archive(
    source_dir: Path,
    dest_dir: Path,
    passphrase: str,
    dry_run: bool = False,
    keep_originals: bool = False,
) -> int:
    """Execute the ECA pipeline for source directory."""
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Error: Source directory does not exist: {source_dir}", file=sys.stderr)
        return 1

    dest_dir.mkdir(parents=True, exist_ok=True)

    # Collect target files
    files_to_archive = sorted([p for p in source_dir.rglob("*.md") if p.is_file()])
    if not files_to_archive:
        print(f"No .md files found in {source_dir} to archive.")
        return 0

    print(f"\n[ECA Pipeline] Found {len(files_to_archive)} markdown files in {source_dir}")

    total_uncompressed = 0
    files_dict: dict[str, bytes] = {}
    files_info: dict[str, dict] = {}
    expected_hashes: dict[str, str] = {}

    for path in files_to_archive:
        rel_path = path.relative_to(source_dir).as_posix()
        data = path.read_bytes()
        sha = compute_sha256(data)
        size = len(data)
        total_uncompressed += size

        files_dict[rel_path] = data
        expected_hashes[rel_path] = sha
        files_info[rel_path] = {
            "size_bytes": size,
            "sha256": sha,
        }
        print(f"  + {rel_path} ({size:,} bytes, sha256: {sha[:12]}...)")

    print(f"\nTotal uncompressed size: {total_uncompressed:,} bytes (~{total_uncompressed/1024:.1f} KB)")

    timestamp_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    archive_base_name = f"wave_1_archive_{timestamp_str}"
    archive_file = dest_dir / f"{archive_base_name}.tar.gz.enc"
    manifest_file = dest_dir / f"{archive_base_name}_manifest.json"

    if dry_run:
        print("\n[DRY RUN] Archive would be created at:")
        print(f"  Container: {archive_file}")
        print(f"  Manifest:  {manifest_file}")
        print(f"  Originals: {'Would be KEPT' if keep_originals else 'Would be SAFELY REMOVED after roundtrip verify'}")
        return 0

    # 1. Compress
    print("\n1. Compressing files into memory (gzip level 9)...")
    compressed_tar = create_tar_gz(files_dict)
    print(f"   Tarball compressed size: {len(compressed_tar):,} bytes")

    # 2. Encrypt
    print("2. Encrypting tarball with AES-256-GCM (PBKDF2-HMAC-SHA256, 600k iter)...")
    container_bytes = encrypt_payload(compressed_tar, passphrase)
    print(f"   Encrypted container size: {len(container_bytes):,} bytes")

    # 3. Write container to disk
    print(f"3. Writing container to disk: {archive_file}")
    archive_file.write_bytes(container_bytes)

    # 4. Self-verification pass (Zero-Trust)
    print("4. Executing automated roundtrip verification pass...")
    try:
        read_back_container = archive_file.read_bytes()
        verify_archive_data(read_back_container, passphrase, expected_hashes)
        print("   [PASS] 100% roundtrip verified! All SHA-256 checksums match perfectly.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] Roundtrip verification failed: {e}", file=sys.stderr)
        print("Aborting. Removing corrupted archive container from disk...", file=sys.stderr)
        if archive_file.exists():
            archive_file.unlink()
        print("Original source files were NOT touched.", file=sys.stderr)
        return 2

    # 5. Write manifest
    print(f"5. Writing audit manifest to: {manifest_file}")
    manifest_data = build_manifest_data(
        source_dir=source_dir,
        files_info=files_info,
        compressed_size=len(container_bytes),
        archive_filename=archive_file.name,
    )
    manifest_file.write_text(json.dumps(manifest_data, indent=2), encoding="utf-8")

    # 6. Safe cleanup of originals
    if keep_originals:
        print("6. Preserving original files in source directory (--keep-originals enabled).")
    else:
        print("6. Safely removing original raw files from source directory...")
        for path in files_to_archive:
            path.unlink()
        print(f"   Removed {len(files_to_archive)} files from {source_dir}.")

    print("\n[SUCCESS] Archiving process completed successfully.")
    print(f"  Archive:  {archive_file}")
    print(f"  Manifest: {manifest_file}")
    print(f"  Saved:    {total_uncompressed - len(container_bytes):,} bytes (Ratio: {manifest_data['compression_ratio']}x)\n")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypt, compress, and archive Stage 1 research files.")
    parser.add_argument(
        "--source",
        type=Path,
        default=PROJECT_ROOT / "research" / "raw" / "Stage 1" / "Wave 1",
        help="Source directory to archive (default: research/raw/Stage 1/Wave 1)",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=PROJECT_ROOT / "research" / "raw" / "Stage 1" / "Archive",
        help="Destination directory for archives (default: research/raw/Stage 1/Archive)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the archiving process without creating files or deleting originals",
    )
    parser.add_argument(
        "--keep-originals",
        action="store_true",
        help="Preserve source files instead of removing them after verification",
    )
    parser.add_argument(
        "--passphrase",
        type=str,
        help="Encryption passphrase (for scripting/testing). If omitted, env var or prompt is used.",
    )
    parser.add_argument(
        "--passphrase-env",
        type=str,
        default="ARCHIVE_PASSPHRASE",
        help="Environment variable name to read passphrase from (default: ARCHIVE_PASSPHRASE)",
    )

    args = parser.parse_args()

    if args.dry_run:
        passphrase = "dry-run-dummy-passphrase"
    else:
        passphrase = get_passphrase(args)

    sys.exit(
        run_archive(
            source_dir=args.source,
            dest_dir=args.dest,
            passphrase=passphrase,
            dry_run=args.dry_run,
            keep_originals=args.keep_originals,
        )
    )


if __name__ == "__main__":
    main()
