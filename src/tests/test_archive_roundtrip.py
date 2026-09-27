"""Unit and integration tests for Encryption-Compression-Archiving (ECA) system."""

import os
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from src.archive_core import (
    AuthenticationError,
    IntegrityError,
    ArchiveError,
    MAGIC_HEADER,
    compute_sha256,
    create_tar_gz,
    extract_tar_gz,
    encrypt_payload,
    decrypt_container,
    verify_archive_data,
    build_manifest_data,
    derive_key,
)


def test_tar_gz_roundtrip():
    files = {
        "file1.md": b"# Hello World\nThis is a markdown file.",
        "sub/file2.txt": b"Nested content here.",
        "unicode.md": "Special chars: ?? ?? ??? ? ??".encode("utf-8"),
    }
    compressed = create_tar_gz(files)
    assert len(compressed) > 0
    extracted = extract_tar_gz(compressed)
    assert extracted == files


def test_encryption_decryption_roundtrip():
    passphrase = "CorrectHorseBatteryStaple123!"
    payload = b"Top secret research brief content for Wave 1."

    container = encrypt_payload(payload, passphrase)
    assert container.startswith(MAGIC_HEADER)
    assert len(container) > len(payload)

    decrypted = decrypt_container(container, passphrase)
    assert decrypted == payload


def test_wrong_passphrase_fails():
    passphrase = "CorrectPassword123!"
    wrong_passphrase = "WrongPassword999!"
    payload = b"Sensitive research claims."

    container = encrypt_payload(payload, passphrase)
    with pytest.raises(AuthenticationError, match="Decryption failed"):
        decrypt_container(container, wrong_passphrase)


def test_tampered_ciphertext_fails():
    passphrase = "TestPassphrase456!"
    payload = b"Unmodified authentic payload."

    container = bytearray(encrypt_payload(payload, passphrase))
    # Tamper with the last byte of the ciphertext
    container[-1] ^= 0xFF

    with pytest.raises(AuthenticationError):
        decrypt_container(bytes(container), passphrase)


def test_tampered_tag_fails():
    passphrase = "TestPassphrase456!"
    payload = b"Unmodified authentic payload."

    container = bytearray(encrypt_payload(payload, passphrase))
    # Tag is located at indices 32..48
    container[35] ^= 0x01

    with pytest.raises(AuthenticationError):
        decrypt_container(bytes(container), passphrase)


def test_invalid_magic_fails():
    passphrase = "TestPassphrase456!"
    payload = b"Payload."

    container = bytearray(encrypt_payload(payload, passphrase))
    container[:4] = b"XXXX"

    with pytest.raises(ArchiveError, match="Invalid magic header"):
        decrypt_container(bytes(container), passphrase)


def test_truncated_container_fails():
    with pytest.raises(ArchiveError, match="Container too small"):
        decrypt_container(b"ECA1too_short", "passphrase")


def test_verify_archive_data_success():
    passphrase = "SecurePassphrase789$"
    files = {
        "A.md": b"Content of A",
        "B.md": b"Content of B",
    }
    hashes = {name: compute_sha256(content) for name, content in files.items()}

    tar_gz_bytes = create_tar_gz(files)
    container = encrypt_payload(tar_gz_bytes, passphrase)

    ok, extracted_hashes = verify_archive_data(container, passphrase, hashes)
    assert ok is True
    assert extracted_hashes == hashes


def test_verify_archive_data_mismatch():
    passphrase = "SecurePassphrase789$"
    files = {"A.md": b"Original A"}
    hashes = {"A.md": "fake_sha256_hash_that_wont_match"}

    tar_gz_bytes = create_tar_gz(files)
    container = encrypt_payload(tar_gz_bytes, passphrase)

    with pytest.raises(IntegrityError, match="Checksum mismatch"):
        verify_archive_data(container, passphrase, hashes)


@settings(max_examples=10, deadline=None)
@given(
    passphrase=st.text(min_size=8, max_size=32),
    data=st.binary(min_size=1, max_size=4096),
)
def test_hypothesis_encrypt_decrypt_invariance(passphrase, data):
    container = encrypt_payload(data, passphrase)
    recovered = decrypt_container(container, passphrase)
    assert recovered == data


def test_cli_archive_and_restore_roundtrip(tmp_path):
    from scripts.archive_stage1 import run_archive
    from scripts.restore_archive import restore_archive

    source_dir = tmp_path / "source"
    archive_dir = tmp_path / "archive"
    restore_dir = tmp_path / "restore"

    source_dir.mkdir()
    (source_dir / "test1.md").write_text("# Test 1\nSome research notes.", encoding="utf-8")
    (source_dir / "test2.md").write_text("# Test 2\nMore notes.", encoding="utf-8")

    passphrase = "SecureIntegrationTestPassphrase123!"

    # 1. Test dry-run
    exit_code = run_archive(source_dir, archive_dir, passphrase, dry_run=True)
    assert exit_code == 0
    assert (source_dir / "test1.md").exists()
    assert len(list(archive_dir.glob("*.tar.gz.enc"))) == 0

    # 2. Run real archive
    exit_code = run_archive(source_dir, archive_dir, passphrase, dry_run=False)
    assert exit_code == 0

    # Originals should be removed from source
    assert not (source_dir / "test1.md").exists()
    assert not (source_dir / "test2.md").exists()

    archives = list(archive_dir.glob("*.tar.gz.enc"))
    manifests = list(archive_dir.glob("*_manifest.json"))
    assert len(archives) == 1
    assert len(manifests) == 1

    # 3. Restore to restore_dir
    container_bytes = archives[0].read_bytes()
    restore_code = restore_archive(container_bytes, passphrase, restore_dir)
    assert restore_code == 0

    # Check restored files
    assert (restore_dir / "test1.md").read_text(encoding="utf-8") == "# Test 1\nSome research notes."
    assert (restore_dir / "test2.md").read_text(encoding="utf-8") == "# Test 2\nMore notes."
