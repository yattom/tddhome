import pytest
from foo.target import *

@pytest.fixture
def vm():
    return VendingMachine()

@pytest.fixture
def vm100():
    vm = VendingMachine()
    vm.insert(Coin.COIN_100)
    return vm

def test_100円コインを投入しないでボタンを押してもコーラは出ない(vm):
    vm.buttons['コーラ'].push()
    assert vm.get_cup() == VendingMachine.EMPTY

def test_ボタンを押さないととコーラが出ない(vm):
    assert vm.get_cup() == VendingMachine.EMPTY

def test_100円コインを投入してからボタンを押すとコーラが出る(vm100):
    vm100.buttons['コーラ'].push()
    assert vm100.get_cup() == 'コーラ'

def test_100円コインを投入してからボタンを押してもレッドブルが出ない(vm100):
    vm100.buttons['レッドブル'].push()
    assert vm100.get_cup() == VendingMachine.EMPTY

def test_200円コインを投入してからボタンを押すとレッドブルが出る(vm):
    vm.insert(Coin.COIN_100)
    vm.insert(Coin.COIN_100)
    vm.buttons['レッドブル'].push()
    assert vm.get_cup() == 'レッドブル'

@pytest.mark.parametrize('item', [
        pytest.param('コーラ', id='コーラ'),
        pytest.param('ウーロン茶', id='ウーロン茶'),
    ])
def test_ボタンによって商品を選べる(vm100, item):
    vm100.buttons[item].push()
    assert vm100.get_cup() == item

def test_最初はボタンは光らない(vm):
    assert not vm.buttons['コーラ'].is_lit()
    assert not vm.buttons['ウーロン茶'].is_lit()
    assert not vm.buttons['レッドブル'].is_lit()

def test_100円いれるとコーラとウーロン茶のボタンが光る(vm100):
    assert vm100.buttons['コーラ'].is_lit()
    assert vm100.buttons['ウーロン茶'].is_lit()
    assert not vm100.buttons['レッドブル'].is_lit()

def test_200円いれるとコーラとウーロン茶とレッドブルのボタンが光る(vm):
    vm.insert(Coin.COIN_100)
    vm.insert(Coin.COIN_100)
    assert vm.buttons['コーラ'].is_lit()
    assert vm.buttons['ウーロン茶'].is_lit()
    assert vm.buttons['レッドブル'].is_lit()

@pytest.mark.parametrize('coin, total', [
    (Coin.COIN_10, 10),
    (Coin.COIN_50, 50),
    (Coin.COIN_100, 100),
    (Coin.COIN_500, 500),
])
def test_各種コインが使える(vm, coin, total):
    vm.insert(coin)
    assert vm.coin == total

def test_投入した合計金額を変更できない(vm):
    with pytest.raises(AttributeError):
        vm.coin = 10
