import random

# NOTES:
# If we don't provide an implementation for
# __lt__, __gt__ or other "dunder" methods, Python
# will provide a default implementation based on the
# defined "dunder" methods with their conditions
# negated
class MSDie:
    """
    Multi-sided die

    Instance variables:
        current_value
        num_sides
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides + 1)
        return self.current_value

    def __str__(self):
        return f"{self.current_value}"

    def __repr__(self):
        return f"MSDie({self.num_sides}) : {self.current_value}"

    def __eq__(self, other):
        return self.current_value == other.current_value

    def __lt__(self, other):
        return self.current_value < other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value

    def __ne__(self, other):
        return self.__eq__(other)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return not self.__le__(other)
