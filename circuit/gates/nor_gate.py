from gates.or_gate import Or

class Nor(Or):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        result = super().perform_gate_logic()

        if result == 1:
            return 0
        else:
            return 1
