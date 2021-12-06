from base.unary_gate import UnaryGate

class Not(UnaryGate):
    def __init__(self, label):
        # Or: super().__init__(label)
        UnaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.get_pin_a()

        if a == 1:
            return 0
        else:
            return 1
