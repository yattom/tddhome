from dataclasses import dataclass

@dataclass
class Item:
    item_no: int
    unit_price: int
    tax_included: bool = False

ITEMS = {
    1: Item(1, 100),
    2: Item(2, 40),
    3: Item(3, 150),
    4: Item(4, 150),
    5: Item(5, 400),
    6: Item(6, 420, True),
    7: Item(7, 440, True),
    8: Item(8, 100),
    9: Item(9, 80),
    10: Item(10, 100),
}

def get_unit_price(item_no):
    return ITEMS[item_no].unit_price

def get_subtotal_of_item(items):
    return sum([ITEMS[item[0]].unit_price * item[1] for item in items])

def get_subtotal_of_item_incl_tax(items):
    return int(sum([
        ITEMS[item[0]].unit_price
         * (item[1] - (item[1] // 10))
         * (1.00 if ITEMS[item[0]].tax_included else 1.08)
        for item in items]))
