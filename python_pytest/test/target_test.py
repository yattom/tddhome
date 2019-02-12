from foo.target import is_reduced_rate_applicable, tax_included, base_price

def test_オロナミンCは軽減税率対象():
    item = "オロナミンC"
    assert is_reduced_rate_applicable(item)

def test_リポビタンDは軽減税率対象外():
    item = "リポビタンD"
    assert not is_reduced_rate_applicable(item)

def test_手巻直火焼き紅しゃけは軽減税率対象():
    item = "手巻直火焼き紅しゃけ"
    assert is_reduced_rate_applicable(item)

def test_おにぎりの税抜価格():
    assert base_price("手巻直火焼き紅しゃけ") == 139

class Test合計金額を求める:
    def test_おにぎり2個(self):
        total = tax_included([("手巻直火焼き紅しゃけ", 2)])
        assert 300 == total

    def test_軽減対象と対象外の組み合わせ(self):
        total = tax_included([
            ("手巻直火焼き紅しゃけ", 2),
            ("キリンチューハイ氷結グレープフルーツ350ml缶", 3),
        ])
        assert 765 == total
