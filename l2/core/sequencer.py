"""Flashblocks-enabled sequencer for EVM L2 (Base-compatible)."""
from __future__ import annotations
import hashlib, time, zlib
from dataclasses import dataclass, field
from typing import List

BATCH_VERSION = 3
MAX_BATCH_BYTES = 256_000
FLASHBLOCK_INTERVAL_MS = 200

@dataclass
class Transaction:
    nonce: int
    gas_limit: int
    to: str
    value: int
    data: bytes
    signature: bytes = field(default_factory=bytes)

@dataclass
class Flashblock:
    index: int
    timestamp: int
    transactions: List[Transaction] = field(default_factory=list)

class BaseSequencer:
    """Base-native sequencer with Flashblocks + x402 paymaster support."""
    def __init__(self):
        self._pending: List[Transaction] = []
        self._flashblocks: List[Flashblock] = []

    def add_tx(self, tx: Transaction) -> bool:
        self._pending.append(tx)
        return True

    def seal_flashblock(self) -> Flashblock:
        fb = Flashblock(index=len(self._flashblocks), timestamp=int(time.time() * 1000))
        fb.transactions.extend(self._pending)
        self._pending.clear()
        self._flashblocks.append(fb)
        return fb
