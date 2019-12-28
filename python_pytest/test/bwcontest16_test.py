from typing import *
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Biweekly Contest 16
        5134
        """
        arr2 = reversed(arr)
        answer = []
        maxv = -1
        for v in arr2:
            answer.append(maxv)
            if maxv < v:
                maxv = v
        return list(reversed(answer))

    def findBestValue(self, arr: List[int], target: int) -> int:
        """
        Biweekly Contest 16
        5135
        """
        arr2 = sorted(arr)
        sum_arr2 = sum(arr2)

        def total(value):
            l = 0
            h = len(arr2)
            while True:
                i = int((l + h) / 2)
                if i == 0 and value < arr2[0]:
                    return value * len(arr2)
                if i == len(arr2) - 1:
                    if arr2[i] < value:
                        return sum_arr2
                    if 0 < i and arr2[i - 1] <= value <= arr2[i]:
                        return sum(arr2[:i - 1]) + value

                if 0 < i and arr2[i - 1] <= value <= arr2[i]:
                    return sum(arr2[:i]) + value * (len(arr2) - i)
                if i < len(arr2) - 1 and arr2[i] <= value <= arr2[i + 1]:
                    return sum(arr2[:i + 1]) + value * (len(arr2) - i - 1)

                if arr2[i] < value:
                    l += int((h - l) / 2)
                else:
                    h -= int((h - l) / 2)

        diffs = {}
        l = 0
        h = 100000
        while True:
            last = (l, h)
            value = int((l + h) / 2)
            diff = target - total(value)
            # print(f"{value=}, {total(value)=}, {diff=}, {arr2=}")
            if abs(diff) not in diffs or value < diffs[abs(diff)]:
                diffs[abs(diff)] = value
            if diff > 0:
                l += int((h - l) / 2)
            else:
                h -= int((h - l) / 2)
            if last == (l, h):
                break

        return diffs[min(diffs.keys())]


    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        Biweekly Contest 16
        5136
        """
        nodes = [root]
        while True:
            next_nodes = []
            for n in nodes:
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
            if not next_nodes:
                return sum([nn.val for nn in nodes])
            nodes = next_nodes
        return 0

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """
        Biweekly Contest 16
        5137. Number of Paths with Max Score
        """
        def cell(x, y):
            if x < 0 or y < 0:
                return "X"
            c = board[y][x]
            if c == "X" or c == "E" or c == "S":
                return c
            else:
                return int(c)
        l = len(board)
        paths = {}
        start = (l - 1, l - 1)
        paths[start] = (0, 1)
        while True:
            new_paths = {}
            for loc in paths:
                maxnum, count = paths[loc]
                def move(x, y):
                    c = cell(x, y)
                    if c == "X":
                        return
                    elif c == "E":
                        if (x, y) not in new_paths:
                            new_paths[(x, y)] = (-1, 0)
                        p = new_paths[(x, y)]
                        if p[0] < maxnum:
                            new_paths[(x, y)] = maxnum, count
                        elif p[0] == maxnum:
                            new_paths[(x, y)] = maxnum, count + p[1]
                    elif type(c) == int or c == "E":
                        if (x, y) not in new_paths:
                            new_paths[(x, y)] = (-1, 0)
                        p = new_paths[(x, y)]
                        if p[0] < maxnum + c:
                            new_paths[(x, y)] = maxnum + c, count
                        elif p[0] == maxnum + c:
                            new_paths[(x, y)] = maxnum + c, count + p[1]
                    else:
                        raise RuntimeError()

                move(loc[0] - 1, loc[1])
                move(loc[0], loc[1] - 1)
                move(loc[0] - 1, loc[1] - 1)

            if len(new_paths) == 1 and (0, 0) in new_paths:
                break
            if len(new_paths) == 0:
                return [0, 0]
            paths = new_paths

        return list(new_paths[(0, 0)])


import pytest

@pytest.fixture
def sut():
    return Solution()


@pytest.mark.parametrize("arr, answer", [
    ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
    ([100], [-1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100, [10] * 999 + [-1]),
])
def test_replaceElements(sut, arr, answer):
    assert sut.replaceElements(arr) == answer

@pytest.mark.parametrize("arr, target, answer", [
    ([4, 9, 3], 10, 3),
    ([2, 3, 5], 10, 5),
    ([60864,25176,27249,21296,20204], 56803, 11361),
    ([100], 10, 10),
    (list(range(1000)), 999*250, 293),
    (list(range(1000)), 1, 0),
])
def test_findBestValue(sut, arr, target, answer):
    assert sut.findBestValue(arr, target) == answer

def test_deepestLeavesSum(sut):
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7, None, None), None), TreeNode(5, None, None)), TreeNode(3, None, TreeNode(6, None, TreeNode(8, None, None))))
    assert sut.deepestLeavesSum(root) == 15


@pytest.mark.parametrize("board, answer", [
    (["E23", "2X2", "12S"], [7, 1]),
    (["E12", "1X1", "21S"], [4, 2]),
    (["E11", "XXX", "11S"], [0, 0]),
    (["EX", "XS"], [0, 1]),
])
def test_replaceElements(sut, board, answer):
    assert sut.pathsWithMaxScore(board) == answer

