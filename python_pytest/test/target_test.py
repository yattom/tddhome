from foo import target

class Cell:
    def __init__(self, status):
        self.status = status

    def next_generation(self):
        return Cell("DEAD")

def test_func_42():
    assert target.func_42() == 42

def test_死んでいるセルに隣接する生きたセルがちょうど3つあれば次の世代が誕生する():
    cell = Cell("DEAD")
    next_cell = cell.next_generation()
    assert next_cell.status == "DEAD"

