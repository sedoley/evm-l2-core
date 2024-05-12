"""Keccak-256 wrapper."""
import hashlib
def keccak256(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()
