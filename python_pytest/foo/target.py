def is_adult(age, sex=None, type=None):
    if type is None:
        return 20 <= age
    if type == "Marriage":
        if sex == "M":
            limit = 18
        elif sex == "F":
            limit = 16
        else:
            raise ValueError()
        return limit <= age
    _, low, high = list(filter(lambda e: e[0] == type, [("Movie", 18, 60), ("Zoo", 15, 64]))[0]
    return low <= age <= high
