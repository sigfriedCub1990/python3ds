from base.binary_gate import BinaryGate

class And(BinaryGate):
    def __init__(self, label):
        # Or: super().__init__(label)
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            return 1
        else:
            return 0
