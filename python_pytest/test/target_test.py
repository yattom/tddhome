import pytest
from foo.target import *

@pytest.fixture()
def vm():
    return VendingMachine()

@pytest.fixture
def coin100(vm):
    vm.insert(Coin.COIN_100)

def test_100円コインを投入しないでボタンを押してもコーラは出ない(vm):
    vm.buttons['コーラ'].push()
    assert vm.get_cup() == VendingMachine.EMPTY

def test_ボタンを押さないととコーラが出ない(vm):
    assert vm.get_cup() == VendingMachine.EMPTY

def test_100円コインを投入してからボタンを押すとコーラが出る(vm, coin100):
    vm.buttons['コーラ'].push()
    assert vm.get_cup() == 'コーラ'

def test_100円コインを投入してからボタンを押してもレッドブルが出ない(vm, coin100):
    vm.buttons['レッドブル'].push()
    assert vm.get_cup() == VendingMachine.EMPTY

def test_200円コインを投入してからボタンを押すとレッドブルが出る(vm):
    vm.insert(Coin.COIN_100)
    vm.insert(Coin.COIN_100)
    vm.buttons['レッドブル'].push()
    assert vm.get_cup() == 'レッドブル'

@pytest.mark.parametrize('item', [
        pytest.param('コーラ', id='コーラ'),
        pytest.param('ウーロン茶', id='ウーロン茶'),
    ])
def test_ボタンによって商品を選べる(vm, coin100, item):
    vm.buttons[item].push()
    assert vm.get_cup() == item

def test_最初はボタンは光らない(vm):
    assert not vm.buttons['コーラ'].is_lit()
    assert not vm.buttons['ウーロン茶'].is_lit()
    assert not vm.buttons['レッドブル'].is_lit()

def test_100円いれるとコーラとウーロン茶のボタンが光る(vm, coin100):
    assert vm.buttons['コーラ'].is_lit()
    assert vm.buttons['ウーロン茶'].is_lit()
    assert not vm.buttons['レッドブル'].is_lit()

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

class Testお釣り計算:
    def test_100円でコーラを買うとお釣りなし(self, vm, coin100):
        vm.buttons['コーラ'].push()
        assert vm.coin == 0

    def test_110円でコーラを買うとお釣り10円(self, vm, coin100):
        vm.insert(Coin.COIN_10)
        vm.buttons['コーラ'].push()
        assert vm.change_pocket == [ Coin.COIN_10 ]
        assert vm.coin == 0

    def test_500円でレッドブルを買うとお釣り300円(self, vm):
        vm.insert(Coin.COIN_500)
        vm.buttons['レッドブル'].push()
        assert vm.change_pocket == [ Coin.COIN_100, Coin.COIN_100, Coin.COIN_100 ]
        assert vm.coin == 0

def test_返却ボタンを押すとお金が戻ってくる(vm, coin100):
    vm.return_button.push()
    assert vm.change_pocket == [ Coin.COIN_100 ]

def test_最初はお釣りボックスは空っぽ(vm):
    assert vm.change_pocket == []
