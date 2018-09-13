class VendingMachine:
    cup = None
    coin = 0

    def push(self):
        if self.coin == 100:
            self.cup = 'コーラ'

    def get_cup(self):
        return self.cup

    def insert_100(self):
        self.coin = 100
