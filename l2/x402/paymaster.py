"""x402 protocol + Base Pay paymaster primitives."""
class X402Paymaster:
    def sponsor_tx(self, tx): ...

    def sponsor(self, tx): ... # Base Pay integration
