from foo import target
from foo.target import Location, Rules, Bag

import pytest

NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"

@pytest.fixture
def origin():
    rules = Rules([
        (NORTH, SOUTH),
        (EAST, WEST),
    ])
    return Location.create_origin(rules)


class TestLocation:
    def test_origin_is_origin(self, origin):
        assert origin is origin

    def test_notrh_is_not_origin(self, origin):
        assert origin is not origin.get(NORTH)

    def test_notrh_of_south_is_origin(self, origin):
        assert origin is origin.get(NORTH).get(SOUTH)

    def test_N_is_NSN(self, origin):
        to_n = origin.get(NORTH)
        to_n_s_n = origin.get(NORTH).get(SOUTH).get(NORTH)
        assert to_n is to_n_s_n

    def test_NE_is_EN(self, origin):
        to_n_e = origin.get(NORTH).get(EAST)
        to_e_n = origin.get(EAST).get(NORTH)
        assert to_n_e is to_e_n

    def test_get_with_multple_directions(self, origin):
        to_n_e_1 = origin.get(NORTH).get(EAST)
        to_n_e_2 = origin.get(NORTH, EAST)
        assert to_n_e_1 is to_n_e_2

    def test_location_knows_coordinate(self, origin):
        to_n_n_e = origin.get(NORTH, NORTH, EAST)
        assert Bag((NORTH, NORTH, EAST)) == to_n_n_e.get_coordinates()

    def test_far_away_location_does_not_increase_cache_size(self, origin):
        size_before = len(origin.system.COORD_OBJ_MAP)

        origin.get(NORTH)
        size_near = len(origin.system.COORD_OBJ_MAP)

        origin.get(*([NORTH] * 100))
        size_far = len(origin.system.COORD_OBJ_MAP)

        assert size_near - size_before == size_far - size_near
