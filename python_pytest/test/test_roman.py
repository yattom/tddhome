import pytest

from foo.roman import roman, Rule, RuleSet, State, ROMAN_RULES

@pytest.mark.parametrize("number,roman_num", [
    (1, "I"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (7, "VII"),
    (9, "IX"),
    (13, "XIII"),
    (14, "XIV"),
    (16, "XVI"),
    (19, "XIX"),
    (20, "XX"),
    (50, "L"),
    (99, "IC"),
    (100, "C"),
])
def test_roman(number, roman_num):
    assert roman(number) == roman_num


class RulesTest:
    def test_rule_applicatble(self):
        rule = Rule(is_applicable=lambda s, n: n == 1,
                    apply=lambda s, n: s + "I",
                    name="1->I")
        sut = RuleSet()
        sut.add_rule(rule)
        assert sut.get_applicable(State("", 1))._rule == rule

def test_count():
    assert "VIV".count("V") == 2
