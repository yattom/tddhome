from typing import *
import math
import random

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        while True:
            a = random.randint(1, n - 1)
            b = n - a
            if '0' not in (str(a) + " " + str(b)):
                return [a, b]

    def minFlips(self, a: int, b: int, c: int) -> int:
        def bn(n):
            s = bin(n)[2:]
            return '0' * (32 - len(s)) + s

        counts = {
            ('0', '0', '0'): 0,
            ('0', '0', '1'): 1,
            ('0', '1', '0'): 1,
            ('0', '1', '1'): 0,
            ('1', '0', '0'): 1,
            ('1', '0', '1'): 0,
            ('1', '1', '0'): 2,
            ('1', '1', '1'): 0,
        }
        sa, sb, sc = bn(a), bn(b), bn(c)
        assert len(sa) == len(sb) == len(sc)
        count = 0
        for i in range(len(sa)):
            aa, bb, cc = sa[i], sb[i], sc[i]
            count += counts[(aa, bb, cc)]

        return count


    def count_independent_networks(self, n, connections):
        nws = list(range(n))
        conmap = {}
        for a, b in connections:
            if a not in conmap:
                conmap[a] = []
            conmap[a].append(b)
            if b not in conmap:
                conmap[b] = []
            conmap[b].append(a)

        while True:
            changed = False
            for i in range(len(nws)):
                if i in conmap:
                    v = min([nws[i]] + [nws[j] for j in conmap[i]])
                    nws[i] = v
                    for j in conmap[i]:
                        if nws[j] != v:
                            nws[j] = v
                            changed = True
            if not changed:
                break

        return len(set(nws))



    def count_independent_networksX(self, n, connections):
        nws = []
        for a, b in sorted(connections):
            found = False
            for nw in nws:
                if a in nw or b in nw:
                    nw.add(a)
                    nw.add(b)
                    found = True
            if not found:
                nws.append(set([a, b]))

        while True:
            changed = False
            for nw_i in range(len(nws)):
                if nws[nw_i] is None:
                    continue
                for nw_j in range(nw_i + 1, len(nws)):
                    if nws[nw_j] is None:
                        continue
                    if nws[nw_i].intersection(nws[nw_j]):
                        nws[nw_i] = nws[nw_i].union(nws[nw_j])
                        nws[nw_j] = None
                        changed = True
            if not changed:
                break
        final_nws = [nw for nw in nws if nw is not None]
        non_solo = set()
        for nw in final_nws:
            non_solo = non_solo.union(nw)
        solo_count = n - len(non_solo)

        return len(final_nws) + solo_count



    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        network_count = self.count_independent_networks(n, connections)
        required_exchange_count = network_count - 1
        neccessary_cables_count = n - 1
        cables_count = len(connections)
        print(f"{network_count=}, {required_exchange_count=}, {neccessary_cables_count=}, {cables_count=}, {cables_count < neccessary_cables_count=}")
        if cables_count < neccessary_cables_count:
            return -1
        return required_exchange_count



import pytest

@pytest.fixture
def sut():
    return Solution()


@pytest.mark.parametrize("n", [
    (2),
    (11),
])
def test_getNoZeroIntegers(sut, n):
    a, b = sut.getNoZeroIntegers(n)
    assert n == a + b
    assert '0' not in (str(a) + " " + str(b))


@pytest.mark.parametrize("a,b,c,answer", [
    (2, 6, 5, 3),
    (4, 2, 7, 1),
    (1, 2, 3, 0),
    (10**0, 0, int('1' * 28, 2), 27),
])
def test_minFlips(sut, a, b, c, answer):
    assert answer == sut.minFlips(a, b, c)


@pytest.mark.parametrize("n,connections,answer", [
    (6, [[0,1], [0,2], [0,3], [1,2], [1,3]], 2),
    (6, [[0,1], [0,2], [0,3], [1,2],], -1),
    (5, [[0,1], [0,2], [3,4], [2,3],], 0),
    (100, [[12,85],[32,95],[45,73],[31,69],[34,97],[72,78],[75,90],[59,90],[47,62],[83,85],[84,93],[12,63],[11,89],[26,37],[81,96],[0,26],[3,4],[42,55],[9,33],[66,95],[38,43],[19,58],[6,25],[1,91],[47,59],[69,72],[24,93],[31,49],[30,60],[0,12],[32,88],[16,46],[12,92],[72,89],[58,59],[9,59],[9,84],[65,90],[59,64],[21,70],[11,28],[11,47],[31,85],[11,65],[59,98],[38,69],[47,48],[18,84],[46,48],[72,74],[46,60],[11,98],[34,52],[39,95],[25,83],[12,57],[69,76],[67,96],[11,60],[6,91],[35,45],[39,61],[25,87],[52,55],[64,65],[32,65],[28,66],[15,32],[17,41],[64,76],[6,19],[17,21],[47,55],[27,62],[14,17],[19,98],[34,44],[54,77],[79,91],[21,23],[5,23],[82,96],[30,54],[42,81],[18,34],[48,67],[52,64],[16,67],[38,78],[16,21],[1,96],[57,58],[20,71],[21,86],[30,66],[41,74],[1,55],[40,58],[49,81],[0,43],[24,32],[43,67],[32,62],[32,56]], 18),
])
def test_makeConnected(sut, n, connections, answer):
    assert answer == sut.makeConnected(n, connections)


@pytest.mark.parametrize("n,connections,answer", [
    (6, [[0, 1], [0,2], [0,3], [1,2], [1,3]], 3),
    (6, [], 6),
    (6, [[0,1], [2,3], [4, 5]], 3),
])
def test_count_independent_networks(sut, n, connections, answer):
    assert answer == sut.count_independent_networks(n, connections)









