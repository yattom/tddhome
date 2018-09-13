class VendingMachine:
    cup = None

    def push(self):
        self.cup = 'コーラ'

    def get_cup(self):
        return self.cup
