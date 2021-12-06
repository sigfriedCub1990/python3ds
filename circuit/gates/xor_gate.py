from base.binary_gate import BinaryGate

class Xor(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        pin_a = self.get_pin_a()
        pin_b = self.get_pin_b()

        if pin_a == 1 and pin_b == 0:
            return 1
        elif pin_a == 0 and pin_b == 1:
            return 1
        else:
            return 0
