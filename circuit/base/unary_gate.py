from base.logical_gate import LogicalGate

class UnaryGate(LogicalGate):
    def __init__(self, label):
        LogicalGate.__init__(self, label)
        self.pin_a = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input(f"Enter Pin A for gate {self.get_label()}: "))
        else:
            return self.pin_a.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            raise RuntimeException("Error: PIN NOT AVAILABLE")
