class Bag:
    def __init__(self, contents=()):
        self.store = {}
        for c in contents:
            self.add(c)

    def add(self, element):
        if element not in self.store:
            self.store[element] = 0
        self.store[element] += 1

    def copy(self):
        new_bag = Bag()
        for element in self.store:
            for i in range(self.store[element]):
                new_bag.add(element)
        return new_bag

    def contains_all(self, other):
        assert type(other) == Bag
        for element in other.store:
            if element not in self.store or self.store[element] < other.store[element]:
                return False
        return True

    def remove_all(self, other):
        assert type(other) == Bag
        if not self.contains_all(other):
            raise ValueError(f"{self} does not contain {other}")
        for element in other.store:
            self.store[element] -= other.store[element]
            if self.store[element] == 0:
                del self.store[element]

    def add_all(self, other):
        assert type(other) == Bag
        for element in other.store:
            for i in range(other.store[element]):
                self.add(element)

    def __eq__(self, other):
        if type(other) is not Bag:
            return False
        return self.store == other.store

    def __hash__(self):
        value = 0
        for element in self.store:
            value += hash(element) * self.store[element]
        return value

    def __iter__(self):
        for element in self.store:
            for i in range(self.store[element]):
                yield element

    def __repr__(self):
        return f"Bag({tuple(self)})"


class Rules:
    def __init__(self, rules):
        self.rules = {}
        for rule in rules:
            self.rules[Bag(rule)] = Bag()

    def apply(self, coordinates):
        resolved = coordinates.copy()
        while True:
            for coordinates in self.rules:
                if resolved.contains_all(coordinates):
                    resolved.remove_all(coordinates)
                    resolved.add_all(self.rules[coordinates])
                    break
            else:
                break
        return resolved


class Location:
    @staticmethod
    def create_origin(rules):
        system = System(rules)
        return Location(system, ())

    def __init__(self, system, coordinates=None):
        if coordinates == ():
            coordinates = Bag()
        self.system = system
        self.hash_value = hash(coordinates)
        self.system.add_coordinates(coordinates, self)

    def get(self, *coordinates):
        absolute_coordinate = self.get_coordinates().copy()
        for c in coordinates:
            absolute_coordinate.add(c)
        resolved_coordinates = self.system.rules.apply(absolute_coordinate)
        if not self.system.has_coordinate(resolved_coordinates):
            self.system.add_coordinates(resolved_coordinates, Location(self.system, resolved_coordinates))
        return self.system.get_obj(resolved_coordinates)

    def get_coordinates(self):
        return self.system.get_coordinates(self)

    def __repr__(self):
        return f"Location(coordinates={self.get_coordinates()})"

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return self.hash_value


class System:
    def __init__(self, rules):
        self.rules = rules
        self.COORD_OBJ_MAP = {}
        self.OBJ_COORD_MAP = {}

    def add_coordinates(self, coordinates, obj):
        self.COORD_OBJ_MAP[coordinates] = obj
        self.OBJ_COORD_MAP[obj] = coordinates

    def get_coordinates(self, obj):
        return self.OBJ_COORD_MAP[obj]

    def get_obj(self, coordinates):
        return self.COORD_OBJ_MAP[coordinates]

    def has_coordinate(self, coordinates):
        return coordinates in self.COORD_OBJ_MAP

