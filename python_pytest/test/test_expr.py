class LiteralExpr:
    def __init__(self, val):
        self.val = str(val)

    def __str__(self):
        return f"{self.val}"


class BinaryExpr:
    def __init__(self, op, expr1, expr2):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        e1 = str(self.expr1)
        if type(self.expr1) != LiteralExpr:
            e1 = f"({e1})"
        e2 = str(self.expr2)
        if type(self.expr2) != LiteralExpr:
            e2 = f"({e2})"

        return f"{e1}{self.op}{e2}"


def insert_digit(base, digit):
    inserted = []
    for i in range(len(base) + 1):
        v = base[0:i] + str(digit) + base[i:]
        if v not in inserted:
            inserted.append(v)
    return inserted


def mix(expr, digit):
    result = []
    if type(expr) == LiteralExpr:
        for var in insert_digit(expr.val, digit):
            result.append(LiteralExpr(var))
    for op in "+*":
        result.append(BinaryExpr(op, expr, LiteralExpr(digit)))
    for op in "-/":
        result.append(BinaryExpr(op, expr, LiteralExpr(digit)))
        result.append(BinaryExpr(op, LiteralExpr(digit), expr))
    if type(expr) == BinaryExpr:
        mixed = mix(expr.expr1, digit)
        for m in mixed:
            result.append(BinaryExpr(expr.op, m, expr.expr2))
        mixed = mix(expr.expr2, digit)
        for m in mixed:
            result.append(BinaryExpr(expr.op, expr.expr1, m))
    return result


def test_expressionize_1():
    e = LiteralExpr(1)
    assert str(e) == '1'


def test_mix_2_to_1():
    e2 = LiteralExpr(2)
    exprs_str = [str(e) for e in mix(e2, 1)]
    assert len(exprs_str) > 0
    assert "12" in exprs_str
    assert "21" in exprs_str
    assert "1+2" not in exprs_str
    assert "2+1" in exprs_str
    assert "1-2" in exprs_str
    assert "2-1" in exprs_str
    assert "1*2" not in exprs_str
    assert "2*1" in exprs_str
    assert "1/2" in exprs_str
    assert "2/1" in exprs_str


def test_mix_9_to_BinaryExpr():
    e = BinaryExpr("+", LiteralExpr(1), LiteralExpr(2))
    exprs_str = [str(e) for e in mix(e, 9)]
    assert len(exprs_str) > 0
    assert "(1+2)+9" in exprs_str
    assert "9+(1+2)" not in exprs_str


def test_mix_9_to_BinaryExpr_with_climbing_down():
    e = BinaryExpr("+", LiteralExpr(1), LiteralExpr(2))
    exprs_str = [str(e) for e in mix(e, 9)]
    assert len(exprs_str) > 0
    assert "(1+9)+2" in exprs_str


def test_insert_a_digit_into_a_number():
    inserted = insert_digit("0000", "1")
    assert len(inserted) == 5
    assert "10000" in inserted
    assert "01000" in inserted
    assert "00100" in inserted
    assert "00010" in inserted
    assert "00001" in inserted


def test_insert_a_digit_into_a_number_without_duplicated():
    inserted = insert_digit("0011", "1")
    assert len(inserted) == 3
    assert "10011" in inserted
    assert "01011" in inserted
    assert "00111" in inserted


if __name__=='__main__':
    import sys
    while True:
        v = sys.stdin.readline().strip()
        exprs = [LiteralExpr(v[0])]
        for d in v[1:]:
            new_exprs = []
            for e in exprs:
                new_exprs += mix(e, d)
            exprs = new_exprs
        print([str(e) for e in new_exprs])
