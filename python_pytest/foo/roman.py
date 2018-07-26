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

    def get_name(self):
        return self._rule.name
    name = property(get_name)


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

    digits = [(5, "V")]  #, (10, "X")]  #, (50, "L"), (100, "C")]
    for i in range(len(digits)):
        num, dgt = digits[i]
        rules.add_rule(
            Rule(is_applicable=lambda s, n: n == num,
                apply=lambda s, n: (dgt, 0),
                name="{}->{}".format(num, dgt))
        )
        rules.add_rule(
            Rule(is_applicable=lambda s, n: 0 < n < num,
                apply=lambda s, n: (roman(num - n) + roman(num), 0),
                name="<{}".format(num))
        )
        if i < len(digits) - 1:
            next_num = digits[i + 1][0]
            print(i, num, next_num)
            rules.add_rule(
                Rule(is_applicable=lambda s, n: num < n < next_num,
                    apply=lambda s, n: (roman(num) + roman(n - num), 0),
                    name=">{}".format(num))
            )
        else:
            rules.add_rule(
                Rule(is_applicable=lambda s, n: num < n < 10,
                    apply=lambda s, n: (roman(num) + roman(n - num), 0),
                    name=">{}".format(num))
            )
#   rules.add_rule(
#       Rule(is_applicable=lambda s, n: n == 5,
#            apply=lambda s, n: ("V", 0),
#            name="5->V")
#   )
#   rules.add_rule(
#       Rule(is_applicable=lambda s, n: 0 < n < 5,
#            apply=lambda s, n: (roman(5 - n) + roman(5), 0),
#            name="<5")
#   )
#   rules.add_rule(
#       Rule(is_applicable=lambda s, n: 5 < n < 10,
#            apply=lambda s, n: (roman(5) + roman(n - 5), 0),
#            name=">5")
#   )
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
    global _rules_log, _log_valid_only
    def log(e):
        if not _rules_log is None:
            _rules_log.append(e)
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
        saved_log = get_log()
        log((state.remain, rule.name))
        new_state = rule.apply(state)
        try:
            ROMAN_RULES.validate(new_state)
            if new_state.remain == 0:
                return new_state.constructed
            else:
                queue += [(new_state, rr) for rr in ROMAN_RULES.get_applicable_rules(new_state)]
        except ValueError as e:
            if _log_valid_only:
                _rules_log = saved_log
            continue

_rules_log = None
_log_valid_only = True

def start_logging(log_valid_only=True):
    global _rules_log, _log_valid_only
    _log_valid_only = log_valid_only
    _rules_log = []

def end_logging():
    global _rules_log
    _rules_log = None

def get_log():
    global _rules_log
    if type(_rules_log) == list:
        return _rules_log[:]
    return None
