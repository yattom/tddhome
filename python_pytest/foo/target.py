class Button:
    def __init__(self, vm, item, price):
        self.vm = vm
        self.item = item
        self.price = price

    def push(self):
        if self.is_lit():
            self.vm.cup = self.item

    def is_lit(self):
        return self.vm.coin >= self.price

class VendingMachine:
    EMPTY = object()

    cup = EMPTY
    coin = 0

    def __init__(self):
        self.buttons = {
            'コーラ': Button(self, 'コーラ', 100),
            'ウーロン茶': Button(self, 'ウーロン茶', 100),
            'レッドブル': Button(self, 'レッドブル', 200),
        }

    def get_cup(self):
        return self.cup

    def insert_100(self):
        self.coin += 100
