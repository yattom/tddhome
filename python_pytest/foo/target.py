class VendingMachine:
    def __init__(self):
        self._coin = 0
    def push(self):
        if self._coin == 100:
            return 'コーラ'
        return None

    def get_coins(self):
        return self._coin

    def deposit(self, coin):
        self._coin = coin
