class Space:
    def __init__(self):
        pass

    def initialize(self, items):
        self._items = items
        lines = items.split("\n")
        self._width = len(lines[0].strip())
        self._height = len(lines)

    def getSize(self):
        return self._width, self._height

    def item(self, row, col):
        return "赤"

    def dump(self):
        return self._items
    
    def finish_moving(self):
        for i in range(self._width - 2):
            l = self.count_same_drops_in_a_row(i)
            if l >= 3:
                self.disappear_consecutive_drops(i, l)

    def count_same_drops_in_a_row(self, col):
        drop = self._items[col]
        count = 0
        for i in range(col, self._width):
            if self._items[i] == drop:
                count += 1
        return count
    
    def disappear_consecutive_drops(self, col, count):
        self._items = self._items[:col] + ("ー" * count) + self._items[col+count:]