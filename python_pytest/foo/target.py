from enum import Enum, auto

class Coin(Enum):
    COIN_10 = auto()
    COIN_50 = auto()
    COIN_100 = auto()
    COIN_500 = auto()

COIN_VALUES = {
    Coin.COIN_10: 10,
    Coin.COIN_50: 50,
    Coin.COIN_100: 100,
    Coin.COIN_500: 500,
}

class Button:
    def __init__(self, vm, item, price):
        self.vm = vm
        self.item = item
        self.price = price

    def push(self):
        if self.is_lit():
            self.vm.cup = self.item
            self.vm.deduct(self.price)
            self.vm.dispense_changes()

    def is_lit(self):
        return self.vm.coin >= self.price


class ReturnButton:
    def __init__(self, vm):
        self.vm = vm

    def push(self):
        self.vm.dispense_changes()

class VendingMachine:
    EMPTY = object()

    cup = EMPTY
    _coin = 0

    def __init__(self):
        self.buttons = {
            'コーラ': Button(self, 'コーラ', 100),
            'ウーロン茶': Button(self, 'ウーロン茶', 100),
            'レッドブル': Button(self, 'レッドブル', 200),
        }
        self.return_button = ReturnButton(self)
        self.change_pocket = []

    def get_cup(self):
        return self.cup

    def insert(self, coin):
        self._coin += COIN_VALUES[coin]

    def deduct(self, price):
        self._coin -= price

    def dispense_changes(self):
        coins = sorted([c for c in Coin], key=lambda c: COIN_VALUES[c], reverse=True)
        changes = []
        for coin in coins:
            while self._coin >= COIN_VALUES[coin]:
                self._coin -= COIN_VALUES[coin]
                changes.append(coin)
        self.change_pocket = changes

    @property
    def coin(self):
        return self._coin

