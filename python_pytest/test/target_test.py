import pytest
from foo.target import *

@pytest.fixture
def vm():
    return VendingMachine()

def test_100円コインを投入しないでボタンを押してもコーラは出ない(vm):
    vm.buttons['コーラ'].push()
    assert vm.get_cup() == VendingMachine.EMPTY

def test_ボタンを押さないととコーラが出ない(vm):
    assert vm.get_cup() == VendingMachine.EMPTY

def test_100円コインを投入してからボタンを押すとコーラが出る(vm):
    vm.insert_100()
    vm.buttons['コーラ'].push()
    assert vm.get_cup() == 'コーラ'

def test_100円コインを投入してからボタンを押してもレッドブルが出ない(vm):
    vm.insert_100()
    vm.buttons['レッドブル'].push()
    assert vm.get_cup() == VendingMachine.EMPTY

def test_200円コインを投入してからボタンを押すとレッドブルが出る(vm):
    vm.insert_100()
    vm.insert_100()
    vm.buttons['レッドブル'].push()
    assert vm.get_cup() == 'レッドブル'

@pytest.mark.parametrize('item', [
        pytest.param('コーラ', id='コーラ'),
        pytest.param('ウーロン茶', id='ウーロン茶'),
    ])
def test_ボタンによって商品を選べる(vm, item):
    vm.insert_100()
    vm.buttons[item].push()
    assert vm.get_cup() == item
