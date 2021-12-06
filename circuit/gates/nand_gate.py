from base.binary_gate import BinaryGate
from gates.and_gate import And

class Nand(And):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        result = super().perform_gate_logic()

        if result == 0:
            return 1
        else:
            return 0
