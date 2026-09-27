"""CLI tool to inspect, verify, and restore files from an encrypted archive."""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.archive_core import (  # noqa: E402
    ArchiveError,
    AuthenticationError,
    IntegrityError,
    compute_sha256,
    decrypt_container,
    extract_tar_gz,
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

    return getpass.getpass("Enter archive passphrase: ")


def list_archive(container_bytes: bytes, passphrase: str) -> int:
    """List contents of archive without extracting to disk."""
    print("Decrypting and decompressing archive in memory...")
    try:
        payload = decrypt_container(container_bytes, passphrase)
    except AuthenticationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ArchiveError as e:
        print(f"Archive error: {e}", file=sys.stderr)
        return 1

    files = extract_tar_gz(payload)
    print(f"\nArchive contains {len(files)} files:\n")
    print(f"{'File':<35} {'Size (bytes)':>14} {'SHA-256 (first 12)':>20}")
    print("-" * 72)
    total_size = 0
    for name, data in sorted(files.items()):
        sha = compute_sha256(data)
        size = len(data)
        total_size += size
        print(f"{name:<35} {size:>14,} {sha[:12]:>20}...")
    print("-" * 72)
    print(f"Total: {len(files)} files, {total_size:,} bytes (~{total_size/1024:.1f} KB)\n")
    return 0


def restore_archive(
    container_bytes: bytes,
    passphrase: str,
    dest_dir: Path,
    overwrite: bool = False,
) -> int:
    """Decrypt and extract all files into dest_dir."""
    print(f"Decrypting and extracting files to: {dest_dir}")
    try:
        payload = decrypt_container(container_bytes, passphrase)
    except AuthenticationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ArchiveError as e:
        print(f"Archive error: {e}", file=sys.stderr)
        return 1

    files = extract_tar_gz(payload)
    dest_dir.mkdir(parents=True, exist_ok=True)

    extracted_count = 0
    for rel_path, data in sorted(files.items()):
        target_path = dest_dir / rel_path
        if target_path.exists() and not overwrite:
            print(f"  [SKIPPED] {rel_path} already exists (use --overwrite to replace)")
            continue
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(data)
        sha = compute_sha256(data)
        print(f"  + Extracted {rel_path} ({len(data):,} bytes, sha: {sha[:12]}...)")
        extracted_count += 1

    print(f"\n[SUCCESS] Extracted {extracted_count} of {len(files)} files to {dest_dir}\n")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect or restore an encrypted ECA archive.")
    parser.add_argument(
        "--archive",
        type=Path,
        required=True,
        help="Path to .tar.gz.enc file",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=PROJECT_ROOT / "research" / "raw" / "Stage 1" / "Wave 1",
        help="Destination directory to restore files to (default: research/raw/Stage 1/Wave 1)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List files inside the archive without writing them to disk",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files in destination directory",
    )
    parser.add_argument(
        "--passphrase",
        type=str,
        help="Decryption passphrase (for scripting/testing). If omitted, env var or prompt is used.",
    )
    parser.add_argument(
        "--passphrase-env",
        type=str,
        default="ARCHIVE_PASSPHRASE",
        help="Environment variable name to read passphrase from (default: ARCHIVE_PASSPHRASE)",
    )

    args = parser.parse_args()

    if not args.archive.exists():
        print(f"Error: Archive file not found: {args.archive}", file=sys.stderr)
        sys.exit(1)

    passphrase = get_passphrase(args)
    container_bytes = args.archive.read_bytes()

    if args.list:
        sys.exit(list_archive(container_bytes, passphrase))
    else:
        sys.exit(restore_archive(container_bytes, passphrase, args.dest, args.overwrite))


if __name__ == "__main__":
    main()
