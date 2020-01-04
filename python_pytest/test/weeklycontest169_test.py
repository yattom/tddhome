from typing import *
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def sumZero(self, n: int) -> List[int]:
        h = int(n / 2)
        if n % 2 == 0:
            return list(range(-h, 0)) + list(range(1, h + 1))
        else:
            return list(range(-h, 0)) + [0] + list(range(1, h + 1))

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def liner(root):
            if root is None:
                return
            stack = []
            node = root
            while True:
                if node.left:
                    stack.append(node)
                    node = node.left
                    continue
                yield node.val
                if node.right:
                    node = node.right
                    continue
                if not stack:
                    break
                node = stack.pop()
                node.left = None

        liner1 = liner(root1)
        liner2 = liner(root2)
        answer = []
        stop1 = stop2 = False
        try:
            v1 = next(liner1)
        except StopIteration:
            stop1 = True
        try:
            v2 = next(liner2)
        except StopIteration:
            stop2 = True
        if stop1 and stop2:
            return []
        while True:
            if stop1:
                answer.append(v2)
                try:
                    v2 = next(liner2)
                except StopIteration:
                    break
            elif stop2:
                answer.append(v1)
                try:
                    v1 = next(liner1)
                except StopIteration:
                    break
            elif v1 < v2:
                answer.append(v1)
                try:
                    v1 = next(liner1)
                except StopIteration:
                    stop1 = True
            else:
                answer.append(v2)
                try:
                    v2 = next(liner2)
                except StopIteration:
                    stop2 = True

        return answer

    def canReach(self, arr: List[int], start: int) -> bool:
        zeros = [i for i, c in enumerate(arr) if c == 0]
        reachable = set([start])
        last_count = 0
        while len(reachable) != last_count:
            last_count = len(reachable)
            for i in list(reachable):
                l = i - arr[i]
                if l in zeros:
                    return True
                if 0 <= l:
                    reachable.add(l)
                r = i + arr[i]
                if r in zeros:
                    return True
                if r < len(arr):
                    reachable.add(r)

        return False

    def isSolvable(self, words: List[str], result: str) -> bool:
        def mappings(chars):
            nums = list(range(10))
            l = len(chars)
            indices = list(range(l))
            while True:
                print(f"{nums=}, {l=}, {indices=}")
                yield {c:nums[indices[i]] for i, c in enumerate(chars)}

                while True:
                    for i in range(len(indices)):
                        indices[i] += 1
                        if indices[i] >= 10:
                            indices[i] -= 10
                        else:
                            break
                    if len(set(indices)) == len(indices):
                        break

        def equal(charnum):
            total = 0
            for w in words:
                w2 = "".join([charnum[c] for c in w])
                if w2[0] == 0:
                    return False
                total += int(w2)
            r2  = "".join([charnum[c] for c in result])
            if r2[0] == 0:
                return False
            return total == int(r2)

        chars = set([c for c in [w for w in words + [result]]])
        overflow = 0
        for i in range(len(result) - 1, -1, -1):
            w_chars = [w[i] for w in words if i < len(w)]
            r_char = result[i]
            chars_of_col = set(w_chars + [r_char])
            possible = mappings(chars_of_col)
            print(f"{list(possible)=}, {chars_of_col=}")

        return False



import pytest

@pytest.fixture
def sut():
    return Solution()


@pytest.mark.parametrize("n", [
    (10),
    (0),
])
def test_sumZero(sut, n):
    actual = sut.sumZero(n)
    print(actual)
    assert sum(actual) == 0
    assert len(actual) == len(set(actual))



N = TreeNode
@pytest.mark.parametrize("root1,root2,answer", [
    (N(2, N(1), N(4)), N(1, N(0), N(3)), [0,1,1,2,3,4]),
    (N(2), N(1), [1,2]),
    (N(2), None, [2]),
    (None, N(2), [2]),
    (None, None, []),
    (N(1, None, N(8)), N(8, N(1)), [1,1,8,8]),
])
def test_getAllElements(sut, root1, root2, answer):
    assert sut.getAllElements(root1, root2) == answer


@pytest.mark.parametrize("arr,start,answer", [
    ([4,2,3,0,3,1,2], 5, True),
    ([4,2,3,0,3,1,2], 0, True),
    ([3,0,2,1,2], 2, False),
])
def test_canReach(sut, arr, start, answer):
    assert sut.canReach(arr, start) == answer


