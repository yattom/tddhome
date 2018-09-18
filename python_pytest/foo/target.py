class VendingMachine:
    def __init__(self):
        self._cup = None

    def get_from_cup(self):
        return self._cup

    def push(self):
        self._cup = 'コーラ'
