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
        for v in self._validations:
            v.validate(constructed, remain)

def validate_appearance(s, c, max):
    if s.count(c) > max:
        raise ValueError("'{}' cannot appear more than {} times. ({} in '{}')".format(c, max, s.count(c), s))
    return True

def validate_order(s, prec, follow):
    if re.search("[{}].*{}".format(''.join(follow), prec), s):
        raise ValueError("'{}' cannot precede '{}'. (s='{}')".format(follow, prec, s))
    return True


def build_roman_rules():
    rules = RuleSet()
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 0 < n <= 3,
             apply=lambda s, n: (s + "I", n - 1),
             name="1->I")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: n == 5,
             apply=lambda s, n: ("V", 0),
             name="5->V")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 0 < n < 5,
             apply=lambda s, n: (roman(5 - n) + roman(5), 0),
             name="<5")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 5 < n < 10,
             apply=lambda s, n: (roman(5) + roman(n - 5), 0),
             name=">5")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: n == 10,
             apply=lambda s, n: ("X", 0),
             name="10->X")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 0 < n < 10,
             apply=lambda s, n: (roman(10 - n) + roman(10), 0),
             name="<10")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 10 < n < 50,
             apply=lambda s, n: (roman(10) + roman(n - 10), 0),
             name=">10")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: n == 50,
             apply=lambda s, n: ("L", 0),
             name="50->L")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 0 < n < 50,
             apply=lambda s, n: (roman(50 - n) + roman(50), 0),
             name="<50")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 50 < n,
             apply=lambda s, n: (roman(50) + roman(n - 50), 0),
             name=">50")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: n == 100,
             apply=lambda s, n: ("C", 0),
             name="100->C")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 0 < n < 100,
             apply=lambda s, n: (roman(100 - n) + roman(100), 0),
             name="<100")
    )
    rules.add_rule(
        Rule(is_applicable=lambda s, n: 100 < n,
             apply=lambda s, n: (roman(100) + roman(n - 100), 0),
             name=">100")
    )
    rules.add_validation(
        Validation(validate=lambda s, n: validate_appearance(s, "V", 1),
                   name="count(V)<=1")
    )
    rules.add_validation(
        Validation(validate=lambda s, n: validate_appearance(s, "X", 3),
                   name="count(X)<=3")
    )
    rules.add_validation(
        Validation(validate=lambda s, n: validate_appearance(s, "L", 1),
                   name="count(L)<=1")
    )
    return rules


ROMAN_RULES = build_roman_rules()


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


def convert(args):
    return roman(*args)
