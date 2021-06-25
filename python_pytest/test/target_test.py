from foo import target
from foo.target import VendingMachine

import pytest

@pytest.fixture
def vending_machine():
    return VendingMachine()


class Testボタンを押す:
    def test_100円投入せずにボタンを押すと何も出ない(self, vending_machine):
        # 前提
        # 実行
        actual = vending_machine.push()
        # 検証
        assert actual == None

    def test_100円投入してからボタンを押すとコーラが出る(self, vending_machine):
        # 前提
        vending_machine.deposit(100)
        # 実行
        actual = vending_machine.push()
        # 検証
        assert actual == 'コーラ'


class Testお金を投入できる:
    def test_最初は0円(self, vending_machine):
        # 前提
        # 実行
        # 検証
        assert vending_machine.get_coins() == 0

    def test_100円投入したら残高は100(self, vending_machine):
        # 前提
        vending_machine.deposit(100)
        # 実行
        # 検証
        assert vending_machine.get_coins() == 100


