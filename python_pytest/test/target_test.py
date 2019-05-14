from foo import target
import pytest


class TicTocToe:
    def __init__(self):
        self._board = "........."

    def dump(self):
        return self._board[0:3] + "\n" + self._board[3:6] + "\n" + self._board[6:9] + "\n"

    def place(self, mark, index):
        self._board = self._board[0:index] + mark + self._board[index + 1:]


def test_初期状態():
    dump = TicTocToe().dump()
    assert dump == "...\n...\n...\n"

@pytest.fixture(scope="module")
def sut():
    print("sut fixture")
    return TicTocToe()

class TestOとXが置ける:
    class Test1個置ける:
        def test_あいだにOを置ける(self, sut):
            sut.place('O', 4)
            dump = sut.dump()
            assert dump == "...\n.O.\n...\n"


        def test_先頭にXを置ける(self, sut):
            sut.place('X', 0)
            dump = sut.dump()
            assert dump == "X..\n...\n...\n"


        def test_終端にXを置ける(self, sut):
            sut.place('X', 8)
            dump = sut.dump()
            assert dump == "...\n...\n..X\n"


    class Test2個置ける:
        def test_中央O_migi上Xを置ける(self, sut):
            sut.place('O', 4)
            sut.place('X', 2)
            dump = sut.dump()
            assert dump == "..X\n.O.\n...\n"

