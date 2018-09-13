import pytest
from foo.target import *

@pytest.fixture
def vm():
    return VendingMachine()

def test_ボタンを押すとコーラが出る(vm):
    vm.push()
    assert vm.get_cup() == 'コーラ'

def test_ボタンを押さないととコーラが出ない(vm):
    assert vm.get_cup() == None
