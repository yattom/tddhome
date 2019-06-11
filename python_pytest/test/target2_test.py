from foo import target

def test_adult():
    assert target.is_adult(20)

def test_child():
    assert not target.is_adult(13)

def test_adule_for_entry():
    assert target.is_adult(13, type="Entry")

