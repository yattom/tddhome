import pytest

from collections import namedtuple

Rule = namedtuple("Rule", ["is_applicable", "apply", "name"])
Validation = namedtuple("Validation", ["validate", "name"])
State = namedtuple("State", ["constructed", "remain"])

class WrappedRule:
    def __init__(self, rule):
        self._rule = rule

    def is_applicable(self, state):
        return self._rule.is_applicable(*state)

    def apply(self, state):
        return State(*self._rule.apply(*state))

    def __repr__(self):
        return "WrappedRule({})".format(self._rule)

class RuleSet:
    def __init__(self):
        self._rules = []
        self._validations = []

    def add_rule(self, rule):
        self._rules.append(rule)

    def add_validation(self, validation):
        self._validations.append(validation)

    def get_applicable(self, state):
        constructed, remain = state
        for r in self._rules:
            if r.is_applicable(constructed, remain):
                return WrappedRule(r)

    def validate(self, state):
        constructed, remain = state
        for v in ROMAN_RULES._validations:
            v.validate(constructed, remain)

def validate_appearance(s, c, max):
    if s.count(c) > max:
        raise ValueError("'{}' cannot appear more than {} times. ({} in '{}')".format(c, max, s.count(c), s))
    return True

ROMAN_RULES = RuleSet()
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 0 < n <= 3,
         apply=lambda s, n: (s + "I", n - 1),
         name="1->I")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: n == 5,
         apply=lambda s, n: ("V", 0),
         name="5->V")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 0 < n < 5,
         apply=lambda s, n: (roman(5 - n) + roman(5), 0),
         name="<5")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 5 < n,
         apply=lambda s, n: (roman(5) + roman(n - 5), 0),
         name=">5")
)
ROMAN_RULES.add_validation(
    Validation(validate=lambda s, n: validate_appearance(s, "V", 1),
               name="count(V)<2")
)


def roman(n):
    state = State("", n)
    while state.remain > 0:
        r = ROMAN_RULES.get_applicable(state)
        new_state = r.apply(state)
        try:
            ROMAN_RULES.validate(new_state)
        except:
            break
        state = new_state
    return state.constructed

def test_1():
    assert roman(1) == "I"

def test_3():
    assert roman(3) == "III"

def test_4():
    assert roman(4) == "IV"

def test_5():
    assert roman(5) == "V"

def test_7():
    assert roman(7) == "VII"

def test_9():
    assert roman(9) == "IX"

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
