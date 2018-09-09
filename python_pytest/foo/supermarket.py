from collections import namedtuple

Service = namedtuple('Service', ['unit', 'price'])

class Item:
    def __init__(self, price, is_tax_included=False, service=None):
        self.price = price
        self.is_tax_included = is_tax_included
        self.service = service

    def get_subtotal(self, amount):
        if self.service:
            return int(amount / self.service.unit) * self.service.price + (amount % self.service.unit) * self.price
        return self.price * amount

ITEMS = {
    1: Item(100, service=Service(3, 280)),
    2: Item(40),
    3: Item(150),
    4: Item(350),
    5: Item(400),
    6: Item(420, is_tax_included=True),
    7: Item(440, is_tax_included=True),
    8: Item(100),
    9: Item(80),
    10: Item(100),
}

TAX_RATE = 0.08

class Cart:
    def __init__(self):
        self.contents = []

    def add_item(self, item_id, amount):
        if item_id not in ITEMS:
            raise ValueError(f"invalid item_id {item_id}")
        if type(amount) != int or amount <= 0:
            raise ValueError(f"invalid amount {amount}")
        self.contents.append((item_id, amount))

    def get_items_tax_excluded(self):
        return [(i, a) for i, a in self.contents if not ITEMS[i].is_tax_included]

    def get_items_tax_included(self):
        return [(i, a) for i, a in self.contents if ITEMS[i].is_tax_included]

    def total(self):
        total_tax_excluded = sum(ITEMS[item_id].get_subtotal(amount)
                                 for item_id, amount
                                 in self.get_items_tax_excluded())
        total_tax_included = sum(ITEMS[item_id].get_subtotal(amount)
                                 for item_id, amount
                                 in self.get_items_tax_included())
        return int(total_tax_excluded * (1 + TAX_RATE)) + total_tax_included


