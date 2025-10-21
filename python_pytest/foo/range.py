class Range:

    def __init__(self):
        self._lower = None
        self._upper = None

    def set_upper(self, upper) -> 'Range':
        if self.has_upper():
            raise RuntimeError()
        if self.has_lower() and not Range.is_valid(self._lower, upper):
            raise ValueError()
        self._upper = upper
        return self

    def upper(self):
        return self._upper

    def set_lower(self, lower) -> 'Range':
        if self.has_lower():
            raise RuntimeError()
        #if self.has_upper() and lower > self._upper:
        if self.has_upper() and not Range.is_valid(lower, self._upper):
            raise ValueError()
        self._lower = lower
        return self

    def lower(self):
        return self._lower

    def has_upper(self) -> bool:
        return self._upper is not None

    def has_lower(self) -> bool:
        return self._lower is not None

    @staticmethod
    def is_valid(lower, upper) -> bool:
        return lower <= upper

    def __str__(self) -> str:
        if not self.has_upper() and not self.has_lower():
            return '[-,-]'
        if not self.has_lower():
            return f'[-,{self._upper}]'
        if not self.has_upper():
            return f'[{self._lower},-]'
        return f'[{self._lower},{self._upper}]'