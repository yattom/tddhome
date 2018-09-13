from foo.target import *

def test_ボタンを押すとコーラが出る():
    sut = VendingMachine()
    sut.push()
    assert sut.get_cup() == 'コーラ'

def test_ボタンを押さないととコーラが出ない():
    sut = VendingMachine()
    assert sut.get_cup() == None
