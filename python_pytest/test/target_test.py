from foo.target import *

def test_ボタンを押すとコーラが出る():
    vm = VendingMachine()
    vm.push()
    actual = vm.get_from_cup()
    assert actual == 'コーラ'

def test_ボタンを押さないとコーラが出ない():
    vm = VendingMachine()
    actual = vm.get_from_cup()
    assert actual == None
