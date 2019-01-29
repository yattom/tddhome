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
            drop = self._items[i]
            l = 0
            for j in range(i, self._width):
                if self._items[j] == drop:
                    l += 1
            if l >= 3:
                self._items = self._items[:i] + ("ー" * l) + self._items[i+l:]
 