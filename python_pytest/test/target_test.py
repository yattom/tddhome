import pytest
from foo.target import *

@pytest.fixture
def vm():
    return VendingMachine()

def test_100円コインを投入しないでボタンを押してもコーラは出ない(vm):
    vm.push()
    assert vm.get_cup() == None

def test_ボタンを押さないととコーラが出ない(vm):
    assert vm.get_cup() == None

def test_100円コインを投入してからボタンを押すとコーラが出る(vm):
    vm.insert_100()
    vm.push()
    assert vm.get_cup() == 'コーラ'

