from foo.target import *


class Button:
    def __init__(self, vm):
        self._vm = vm

    def push(self):
        if self._vm._money == 100:
            self._vm.dispense('Cola')


class VendingMechine:
    def __init__(self):
        self._cup = None
        self._money = 0
        self._buttons = [ Button(self) ]

    def pop_from_cup(self):
        cup = self._cup
        self._cup = None
        return cup

    def dispense(self, item):
        self._cup = item

    def insert_coin(self, money):
        self._money = money

    def get_buttons(self, index):
        return self._buttons[index]


import pytest

@pytest.fixture
def vm():
    return VendingMechine()

def test_empty(vm):
    assert vm.pop_from_cup() == None

def test_cannot_buy_without_money(vm):
    vm.get_buttons(0).push()
    assert vm.pop_from_cup() == None

def test_pop_from_cup_makes_cup_empty(vm):
    vm.get_buttons(0).push()
    vm.pop_from_cup()
    assert vm.pop_from_cup() == None

def test_insert_coin_and_buy(vm):
    vm.insert_coin(100)
    vm.get_buttons(0).push()
    assert vm.pop_from_cup() == 'Cola'



    
