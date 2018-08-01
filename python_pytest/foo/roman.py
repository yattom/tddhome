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

def validate_sequence(s, c, max):
    if c*(max + 1) in s:
        raise ValueError("'{}' cannot repeat more than {} times. ({} in '{}')".format(c, max, s.count(c), s))
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

    digits = [(5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M")]
    for i in range(len(digits)):
        num, dgt = digits[i]
        # below here, lambda a, b, c=c: ... is to prevent value of c from overwritten
        # by later iteration of a loop.
        # see https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
        rules.add_rule(
            Rule(is_applicable=lambda s, n, num=num: n == num,
                apply=lambda s, n, dgt=dgt: (dgt, 0),
                name="{}->{}".format(num, dgt))
        )
        rules.add_rule(
            Rule(is_applicable=lambda s, n, num=num: 0 < n < num,
                apply=lambda s, n, num=num: (roman(num - n) + roman(num), 0),
                name="<{}".format(num))
        )
        if i < len(digits) - 1:
            next_num = digits[i + 1][0]
            rules.add_rule(
                Rule(is_applicable=lambda s, n, num=num, next_num=next_num: num < n < next_num,
                    apply=lambda s, n, num=num: (roman(num) + roman(n - num), 0),
                    name=">{}".format(num))
            )
        else:
            rules.add_rule(
                Rule(is_applicable=lambda s, n, num=num: num < n,
                    apply=lambda s, n, num=num: (roman(num) + roman(n - num), 0),
                    name=">{}".format(num))
            )

    for dgt in "VLD":
        rules.add_validation(
            Validation(validate=lambda s, n, dgt=dgt: validate_appearance(s, dgt, 1),
                    name="count({})<=1".format(dgt))
        )
    for dgt in "IXCM":
        rules.add_validation(
            Validation(validate=lambda s, n, dgt=dgt: validate_sequence(s, dgt, 3),
                    name="count({})<=3".format(dgt))
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
