class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def is_adult(self):
        return 20 <= self._age

    def is_child(self):
        return self._age < 20

    def __repr__(self):
        return f"User(name={repr(self._name)}, age={repr(self._age)})"

    def name(self):
        return self._name
