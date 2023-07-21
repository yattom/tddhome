class ClosedRange:
    def __init__(self, lower, upper):
        if upper < lower:
            raise ValueError()
        self.lower = lower
        self.upper = upper

    def include(self, point):
        return self.lower <= point <= self.upper

    def contains_whole(self, other):
        return False

    def __str__(self):
        return f"[{self.lower},{self.upper}]"

    def __eq__(self, other):
        if not isinstance(other, ClosedRange):
            return False
        return self.upper == other.upper and self.lower == other.lower

