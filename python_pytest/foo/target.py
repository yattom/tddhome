class VendingMachine:
    def __init__(self):
        self._cup = None
        self._coin = 0
        self._buttons = [
            Button(self, 'コーラ', 100),
            Button(self, 'ウーロン茶', 100),
            Button(self, 'レッドブル', 200),
        ]

    def get_from_cup(self):
        return self._cup

    def insert100(self):
        self._coin += 100

    def select_button(self, idx):
        return self._buttons[idx]

    def coin_remain(self):
        return self._coin

class Button:
    def __init__(self, vm, beverage, price):
        self._vm = vm
        self._bevarage = beverage
        self._price = price

    def push(self):
        if self._vm._coin == self._price:
            self._vm._cup = self._bevarage
            self._vm._coin -= self._price
