from foo.target import *
import pytest

@pytest.fixture
def vm():
    # 前処理
    yield VendingMachine()
    # 後処理

def test_100円入れずにボタンを押すとコーラが出ない(vm):
    vm.select_button(0).push()
    assert vm.get_from_cup() == None

def test_ボタンを押さないとコーラが出ない(vm):
    assert vm.get_from_cup() == None

@pytest.mark.parametrize('idx,bevarage', [
    (0, 'コーラ'),
    (1, 'ウーロン茶'),
])
def test_押したボタンに応じて飲み物が出る(vm, idx, bevarage):
    vm.insert100()
    vm.select_button(idx).push()
    assert vm.get_from_cup() == bevarage
