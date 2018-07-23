import pytest
import re

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
        self._rules.append(WrappedRule(rule))

    def add_validation(self, validation):
        self._validations.append(validation)

    def get_applicable(self, state):
        for r in self._rules:
            if r.is_applicable(state):
                return r

    def get_applicable_rules(self, state):
        return [r for r in self._rules if r.is_applicable(state)]

    def validate(self, state):
        constructed, remain = state
        for v in ROMAN_RULES._validations:
            v.validate(constructed, remain)

def validate_appearance(s, c, max):
    if s.count(c) > max:
        raise ValueError("'{}' cannot appear more than {} times. ({} in '{}')".format(c, max, s.count(c), s))
    return True

def validate_order(s, prec, follow):
    if re.search("[{}].*{}".format(''.join(follow), prec), s):
        raise ValueError("'{}' cannot precede '{}'. (s='{}')".format(follow, prec, s))
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
    Rule(is_applicable=lambda s, n: 5 < n < 10,
         apply=lambda s, n: (roman(5) + roman(n - 5), 0),
         name=">5")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: n == 10,
         apply=lambda s, n: ("X", 0),
         name="10->X")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 0 < n < 10,
         apply=lambda s, n: (roman(10 - n) + roman(10), 0),
         name="<10")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 10 < n < 50,
         apply=lambda s, n: (roman(10) + roman(n - 10), 0),
         name=">10")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: n == 50,
         apply=lambda s, n: ("L", 0),
         name="50->L")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 0 < n < 50,
         apply=lambda s, n: (roman(50 - n) + roman(50), 0),
         name="<50")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 50 < n,
         apply=lambda s, n: (roman(50) + roman(n - 50), 0),
         name=">50")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: n == 100,
         apply=lambda s, n: ("C", 0),
         name="100->C")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 0 < n < 100,
         apply=lambda s, n: (roman(100 - n) + roman(100), 0),
         name="<100")
)
ROMAN_RULES.add_rule(
    Rule(is_applicable=lambda s, n: 100 < n,
         apply=lambda s, n: (roman(100) + roman(n - 100), 0),
         name=">100")
)
ROMAN_RULES.add_validation(
    Validation(validate=lambda s, n: validate_appearance(s, "V", 1),
               name="count(V)<=1")
)
ROMAN_RULES.add_validation(
    Validation(validate=lambda s, n: validate_appearance(s, "X", 3),
               name="count(X)<=3")
)
ROMAN_RULES.add_validation(
    Validation(validate=lambda s, n: validate_appearance(s, "L", 1),
               name="count(L)<=1")
)


def roman(n):
    init_state = State("", n)
    queue = [(init_state, r) for r in ROMAN_RULES.get_applicable_rules(init_state)]
    resolved = set()
    while queue:
        queue.sort(key=lambda e: e[0].remain)
        trial = queue.pop(0)
        if trial in resolved:
            continue
        resolved.add(trial)
        state, rule = trial
        new_state = rule.apply(state)
        try:
            ROMAN_RULES.validate(new_state)
            if new_state.remain == 0:
                return new_state.constructed
            else:
                queue += [(new_state, rr) for rr in ROMAN_RULES.get_applicable_rules(new_state)]
        except ValueError as e:
            continue


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
