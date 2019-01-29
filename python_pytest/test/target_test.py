from foo import Space
import pytest

'''
TODO
- 3つ縦か横に同じ色がそろうと消える
  - 1列, 横3こ並びのみ
- 消えた後は空間になり、上から落ちてくる
- 一番上の空間には、ランダムに画面外から落ちてくる
- 移動できる制限時間は4秒間
- ドロップを指で掴んで動かせる
- ドロップはタテヨコ斜めに動かせる
- 動かした先のドロップと入れ替わる
- 指を離すと移動がおわる
- 移動が終わると消える
- ドロップは横6列縦5行
  x サイズを自由に指定できるようにする
- 初期状態はドロップはランダム
- ドロップは5色＋ハートの6種類
'''

@pytest.fixture
def space():
    return Space()

@pytest.fixture
def space赤青赤(space):
    space.initialize("赤青赤")
    return space

@pytest.fixture
def space赤赤赤(space):
    space.initialize("赤赤赤")
    return space


def test_初期状態が作れる_すべて赤(space):
    space.initialize("""赤赤赤赤赤赤
赤赤赤赤赤赤
赤赤赤赤赤赤
赤赤赤赤赤赤
赤赤赤赤赤赤""")
    width, height = space.getSize()
    assert width == 6 and height == 5
    assert "赤" == space.item(0, 0)
    expected = """赤赤赤赤赤赤
赤赤赤赤赤赤
赤赤赤赤赤赤
赤赤赤赤赤赤
赤赤赤赤赤赤"""
    assert expected == space.dump()


def test_初期状態が作れる_3x1(space赤赤赤):
    width, height = space赤赤赤.getSize()
    assert width == 3 and height == 1
    assert "赤" == space赤赤赤.item(0, 0)
    expected = "赤赤赤"
    assert expected == space赤赤赤.dump()


def test_横に3つそろうと消える(space赤赤赤):
    space赤赤赤.finish_moving()
    assert "ーーー" == space赤赤赤.dump()


def test_横に3つそろわないと消えない(space赤青赤):
    space赤青赤.finish_moving()
    assert "赤青赤" == space赤青赤.dump()


def test_初期状態が作れる_6x1(space):
    space.initialize("赤赤赤赤赤赤")
    width, height = space.getSize()
    assert width == 6 and height == 1


def test_横に4つそろうと消える(space):
    space.initialize("青青赤赤赤赤")
    space.finish_moving()
    assert "青青ーーーー" == space.dump()
