def confirm_age(age):
    if age < 18:
        return "未成年"
    if age < 20:
        return "成年 (飲酒不可)"
    else:
        return "成年"
    return "未定義"


def calc_ticket(age):
    if age < 6:
        return 0
    if age < 12:
        return 800
    return 1600

