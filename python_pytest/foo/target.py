import math

REDUCED_RATE_APPLICABLE_ITEMS = [
    "オロナミンC",
    "手巻直火焼き紅しゃけ",
]

PRICE_LIST = {
    "手巻直火焼き紅しゃけ": 139,
    "キリンチューハイ氷結グレープフルーツ350ml缶": 141,
}

TAX_RATE = 1.10
TAX_RATE_REDUCED = 1.08

def is_reduced_rate_applicable(item):
    return item in REDUCED_RATE_APPLICABLE_ITEMS

def base_price(item):
    return PRICE_LIST[item]

def tax_included(items):
    total = 0
    total_reduced = 0
    for item, count in items:
        if is_reduced_rate_applicable(item):
            total_reduced += base_price(item) * count
        else:
            total += base_price(item) * count

    return int(math.floor(total_reduced * TAX_RATE_REDUCED + total * TAX_RATE))
