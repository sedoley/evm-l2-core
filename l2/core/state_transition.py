"""EVM state-transition with Azul-era upgrades."""
from dataclasses import dataclass
from typing import Dict

@dataclass
class Account: ...

class StateTransitionEngine:
    def apply_batch(self, batch) -> bytes: ...
