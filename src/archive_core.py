"""Core library for Encryption-Compression-Archiving (ECA) protocol.

Implements lossless gzip compression and AES-256-GCM authenticated encryption
with PBKDF2-HMAC-SHA256 key derivation.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import tarfile
import time
from pathlib import Path
from typing import Any, Dict, Tuple

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

MAGIC_HEADER = b"ECA1"
SALT_LEN = 16
NONCE_LEN = 12
TAG_LEN = 16
HEADER_LEN = len(MAGIC_HEADER) + SALT_LEN + NONCE_LEN + TAG_LEN  # 4 + 16 + 12 + 16 = 48 bytes
PBKDF2_ITERATIONS = 600_000
KEY_LEN = 32  # 256 bits


class ArchiveError(Exception):
    """Base exception for archive operations."""


class AuthenticationError(ArchiveError):
    """Raised when authentication tag verification or passphrase fails."""


class IntegrityError(ArchiveError):
    """Raised when file checksums do not match expected values."""


def compute_sha256(data: bytes) -> str:
    """Compute SHA-256 hex digest of bytes."""
    return hashlib.sha256(data).hexdigest()


def compute_file_sha256(path: Path) -> str:
    """Compute SHA-256 hex digest of a file on disk."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def derive_key(passphrase: str, salt: bytes, iterations: int = PBKDF2_ITERATIONS) -> bytes:
    """Derive 256-bit AES key from passphrase and salt using PBKDF2-HMAC-SHA256."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LEN,
        salt=salt,
        iterations=iterations,
    )
    return kdf.derive(passphrase.encode("utf-8"))


def create_tar_gz(files_dict: Dict[str, bytes], mtime: int | None = None) -> bytes:
    """Pack dictionary of {relative_path: file_bytes} into an in-memory tar.gz archive.
    
    Paths are normalized to forward slashes to ensure platform independence.
    """
    if mtime is None:
        mtime = int(time.time())

    out = io.BytesIO()
    with tarfile.open(fileobj=out, mode="w:gz", compresslevel=9) as tar:
        for rel_path, data in sorted(files_dict.items()):
            norm_name = rel_path.replace("\\", "/")
            ti = tarfile.TarInfo(name=norm_name)
            ti.size = len(data)
            ti.mtime = mtime
            ti.mode = 0o644
            tar.addfile(ti, io.BytesIO(data))
    return out.getvalue()


def extract_tar_gz(compressed_bytes: bytes) -> Dict[str, bytes]:
    """Extract in-memory tar.gz archive into a dictionary of {relative_path: file_bytes}."""
    inp = io.BytesIO(compressed_bytes)
    result = {}
    with tarfile.open(fileobj=inp, mode="r:gz") as tar:
        for member in tar.getmembers():
            if member.isfile():
                f = tar.extractfile(member)
                if f is not None:
                    result[member.name] = f.read()
    return result


def encrypt_payload(payload: bytes, passphrase: str) -> bytes:
    """Encrypt payload using AES-256-GCM with PBKDF2-derived key.
    
    Format:
    [0:4]   Magic (b"ECA1")
    [4:20]  Salt (16 bytes)
    [20:32] Nonce (12 bytes)
    [32:48] Tag (16 bytes)
    [48:]   Ciphertext
    """
    salt = os.urandom(SALT_LEN)
    nonce = os.urandom(NONCE_LEN)
    key = derive_key(passphrase, salt)

    aesgcm = AESGCM(key)
    # AESGCM.encrypt appends the 16-byte tag to the ciphertext
    ct_with_tag = aesgcm.encrypt(nonce, payload, associated_data=MAGIC_HEADER)
    ciphertext = ct_with_tag[:-TAG_LEN]
    tag = ct_with_tag[-TAG_LEN:]

    container = io.BytesIO()
    container.write(MAGIC_HEADER)
    container.write(salt)
    container.write(nonce)
    container.write(tag)
    container.write(ciphertext)
    return container.getvalue()


def decrypt_container(container_bytes: bytes, passphrase: str) -> bytes:
    """Decrypt container bytes back to plaintext payload.
    
    Validates magic bytes, extracts salt/nonce/tag, and authenticates ciphertext.
    """
    if len(container_bytes) < HEADER_LEN:
        raise ArchiveError(f"Container too small: {len(container_bytes)} bytes (minimum {HEADER_LEN} bytes)")

    magic = container_bytes[:4]
    if magic != MAGIC_HEADER:
        raise ArchiveError(f"Invalid magic header: {magic!r}, expected {MAGIC_HEADER!r}")

    salt = container_bytes[4:20]
    nonce = container_bytes[20:32]
    tag = container_bytes[32:48]
    ciphertext = container_bytes[48:]

    key = derive_key(passphrase, salt)
    aesgcm = AESGCM(key)

    # Reconstruct ciphertext + tag for cryptography's AESGCM API
    data_to_decrypt = ciphertext + tag
    try:
        payload = aesgcm.decrypt(nonce, data_to_decrypt, associated_data=MAGIC_HEADER)
    except InvalidTag as e:
        raise AuthenticationError("Decryption failed: incorrect passphrase or corrupted/tampered archive.") from e

    return payload


def verify_archive_data(
    container_bytes: bytes,
    passphrase: str,
    expected_hashes: Dict[str, str],
) -> Tuple[bool, Dict[str, str]]:
    """Perform full roundtrip decryption, decompression, and checksum validation.
    
    Returns (True, extracted_hashes) if all hashes match exactly, else raises IntegrityError.
    """
    payload = decrypt_container(container_bytes, passphrase)
    files = extract_tar_gz(payload)

    extracted_hashes = {name: compute_sha256(content) for name, content in files.items()}

    # Check for missing or extra files
    expected_set = set(expected_hashes.keys())
    extracted_set = set(extracted_hashes.keys())

    if expected_set != extracted_set:
        diff_missing = expected_set - extracted_set
        diff_extra = extracted_set - expected_set
        raise IntegrityError(
            f"Archive file list mismatch: missing {diff_missing}, extra {diff_extra}"
        )

    # Check every hash
    mismatches = []
    for name, exp_hash in expected_hashes.items():
        act_hash = extracted_hashes[name]
        if exp_hash != act_hash:
            mismatches.append(f"{name}: expected {exp_hash}, got {act_hash}")

    if mismatches:
        raise IntegrityError(f"Checksum mismatch in roundtrip verification:\n" + "\n".join(mismatches))

    return True, extracted_hashes


def build_manifest_data(
    source_dir: Path,
    files_info: Dict[str, Dict[str, Any]],
    compressed_size: int,
    archive_filename: str,
) -> Dict[str, Any]:
    """Generate manifest dictionary for audit and traceability."""
    total_uncompressed = sum(f["size_bytes"] for f in files_info.values())
    ratio = (total_uncompressed / compressed_size) if compressed_size > 0 else 1.0

    return {
        "format": "ECA-v1",
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "archive_file": archive_filename,
        "source_directory": str(source_dir.resolve()),
        "file_count": len(files_info),
        "total_uncompressed_bytes": total_uncompressed,
        "total_compressed_bytes": compressed_size,
        "compression_ratio": round(ratio, 2),
        "verification_status": "VERIFIED_OK",
        "cipher": "AES-256-GCM",
        "kdf": f"PBKDF2-HMAC-SHA256 ({PBKDF2_ITERATIONS} iterations)",
        "files": [
            {
                "path": rel_path,
                "size_bytes": info["size_bytes"],
                "sha256": info["sha256"],
            }
            for rel_path, info in sorted(files_info.items())
        ],
    }
