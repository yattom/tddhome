class VendingMachine:
    def __init__(self):
        self._cup = None
        self._coin = 0
        self._buttons = [
            Button(self, 'コーラ'),
            Button(self, 'ウーロン茶'),
        ]

    def get_from_cup(self):
        return self._cup

    def insert100(self):
        self._coin = 100

    def select_button(self, idx):
        return self._buttons[idx]


class Button:
    def __init__(self, vm, beverage):
        self._vm = vm
        self._bevarage = beverage

    def push(self):
        if self._vm._coin == 100:
            self._vm._cup = self._bevarage
