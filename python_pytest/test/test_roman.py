import pytest

from foo.roman import roman, Rule, RuleSet, State, ROMAN_RULES, start_logging, end_logging, get_log

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
    (39, "XXXIX"),
    (50, "L"),
    (99, "IC"),
    (100, "C"),
    (400, "CD"),
    (450, "CDL"),
    (900, "CM"),
    (999, "IM"),
    (3000, "MMM"),
    (3800, "MMMDCCC"),
    (3900, "MMMCM"),
    (3999, "MMMIM"),
])
def test_roman(number, roman_num):
    assert roman(number) == roman_num


@pytest.mark.parametrize("number,expected_rules", [
    (1, [(1, "1->I")]),
    (4, [(4, '<5'), (1, "1->I"), (5, '5->V')]),
    (8, [(8, '>5'), (5, '5->V'), (3, '1->I'), (2, '1->I'), (1, '1->I')]),
    (16, [(16, '>10'), (10, '10->X'), (6, '>5'), (5, '5->V'), (1, '1->I')]),
    (48, [(48, '<50'), (2, '1->I'), (1, '1->I'), (50, '50->L')]),
])
def test_roman_applied_rules(number, expected_rules):
    start_logging(log_valid_only=True)
    applied_rules = []
    roman_num = roman(number)
    applied_rules = get_log()
    end_logging()
    assert applied_rules == expected_rules

@pytest.mark.parametrize("number,expected_rules", [
    (1, [(1, "1->I")]),
    (4, [(4, '<5'), (1, "1->I"), (5, '5->V')]),
    (8, [(8, '>5'), (5, '5->V'), (3, '1->I'), (2, '1->I'), (1, '1->I')]),
    (16, [(16, '>10'), (10, '10->X'), (6, '>5'), (5, '5->V'), (1, '1->I')]),
    (48, [(48, '>10'), (10, '10->X'), (38, '>10'), (10, '10->X'), (28, '>10'), (10, '10->X'), (18, '>10'), (10, '10->X'), (8, '>5'), (5, '5->V'), (3, '1->I'), (2, '1->I'), (1, '1->I'), (48, '<50'), (2, '1->I'), (1, '1->I'), (50, '50->L')]),
])
def test_roman_tried_rules(number, expected_rules):
    start_logging(log_valid_only=False)
    applied_rules = []
    roman_num = roman(number)
    applied_rules = get_log()
    end_logging()
    assert applied_rules == expected_rules

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
