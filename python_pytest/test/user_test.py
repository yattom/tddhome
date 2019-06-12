import pytest
from user import User


def test_20歳は成人():
    sut = User(name='yattom', age=20)
    assert sut.is_adult()

def test_10歳は子ども():
    sut = User(name='yattom', age=10)
    assert sut.is_child()


class TestUser:
    def test_20歳は成人(self):
        sut = User(name='yattom', age=20)
        assert sut.is_adult()

    def test_10歳は子ども(self):
        sut = User(name='yattom', age=10)
        assert sut.is_child()


@pytest.fixture
def clear_db():
    pass  # データベースを初期化する処理

@pytest.fixture
def adult():
    return User(name='yattom', age=20)

@pytest.fixture
def child():
    return User(name='yattomy', age=10)

def test_20歳は成人(clear_db, adult):
    assert adult.is_adult()

def test_10歳は子ども(clear_db, child):
    assert child.is_child()

def test_名前(adult):
    assert "yatomm" == adult.name()


def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

def test_file_read(monkeypatch):
    import io
    dummy_stream = io.StringIO("a\nb\nc\n")
    monkeypatch.setitem(__builtins__, 'open', lambda a, b: dummy_stream)
    lines = read_file('dummyfilename')
    assert lines == ['a\n', 'b\n', 'c\n']