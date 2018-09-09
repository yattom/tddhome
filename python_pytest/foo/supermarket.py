ITEMS = {
    1: 100,
    2: 40,
    3: 150,
    4: 350,
    5: 400,
    6: 420,
    7: 440,
    8: 100,
    9: 80,
    10: 100,
}

class Cart:
    def __init__(self):
        self.contents = []

    def add_item(self, item_id, amount):
        if item_id not in ITEMS:
            raise ValueError(f"invalid item_id {item_id}")
        if type(amount) != int or amount <= 0:
            raise ValueError(f"invalid amount {amount}")
        self.contents.append((item_id, amount))

    def total(self):
        return sum([ITEMS[item_id] * amount for item_id, amount in self.contents])

