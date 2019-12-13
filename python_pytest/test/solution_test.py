from typing import *
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        Contest 166
        1283. Find the Smallest Divisor Given a Threshold
        https://leetcode.com/contest/weekly-contest-166/problems/find-the-smallest-divisor-given-a-threshold/
        """
        def div(a, b):
            return math.ceil(a / b)

        def val(nums, divisor):
            return sum([div(n, divisor) for n in nums])

        l = 1
        h = max(nums)
        while True:
            d = int((l + h) / 2)
            m = val(nums, d)
            #print(f"{l=}, {h=}, {d=}, {m=}, {threshold=}")
            if m == threshold:
                break
            if h - l <= 1:
                break
            if m > threshold:
                l = d
            else:
                h = d

        while True:
            if val(nums, d) > threshold:
                if val(nums, d + 1) <= threshold:
                    return d + 1
                else:
                    d += 1
            if val(nums, d) <= threshold:
                if d == 1:
                    return d
                if val(nums, d - 1) > threshold:
                    return d
                else:
                    d -= 1


    def minFlips(self, mat: List[List[int]]) -> int:
        """
        Contest 166
        1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
        https://leetcode.com/contest/weekly-contest-166/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
        """
        def flip(mat, row, col):
            def flipCell(mat, row, col):
                if 0 <= row < m and 0 <= col < n:
                    mask = 1 << (row * n + col)
                    if mat & mask == 0:
                        mat |= mask
                    else:
                        mat &= (~mask)
                return mat
            flipped = mat
            flipped = flipCell(flipped, row, col)
            flipped = flipCell(flipped, row - 1, col)
            flipped = flipCell(flipped, row, col - 1)
            flipped = flipCell(flipped, row + 1, col)
            flipped = flipCell(flipped, row, col + 1)
            return flipped

        def toKey(mat):
            return int(''.join([''.join([str(n) for n in r]) for r in mat]), 2)

        def isZero(mat):
            return mat == 0

        m = len(mat)
        n = len(mat[0])
        mat_int = toKey(mat)
        to_cover: List[Tuple(int, int)] = [ (mat_int, 0) ]
        covered: Set[int] = set()

        while to_cover:
            to_cover_new = []
            for mat_step, step_count in to_cover:
                covered.add(mat_step)
                if isZero(mat_step):
                    # print(f"Zero!! {mat_step=}")
                    return step_count

                for r in range(m):
                    for c in range(n):
                        flipped = flip(mat_step, r, c)
                        # print(bin(flipped), r, c, bin(mat_step))
                        if flipped not in covered:
                            to_cover_new.append((flipped, step_count + 1))

            to_cover = to_cover_new
            # print(to_cover, covered)

        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two Sum
        https://leetcode.com/problems/two-sum/
        """
        num_map: Map[int, int] = {}
        for i, n in enumerate(nums):
            if n not in num_map:
                num_map[n] = []
            num_map[n].append(i)
        for n in num_map:
            if (target - n) in num_map:
                if n == target - n:
                    if len(num_map[n]) < 2:
                        continue
                    return num_map[n]
                return sorted([num_map[n][0], num_map[target - n][0]])

import pytest

@pytest.fixture
def sut():
    return Solution()

@pytest.mark.parametrize('nums,threshold,answer', [
        ([1,2,5,9], 6, 5),
        ([16,79,6,43,53], 172, 2)
    ])
def test_smallestDivisor(sut, nums, threshold, answer):
    assert answer == sut.smallestDivisor(nums, threshold)


@pytest.mark.parametrize('mat,answer', [
        ([[0,0],[0,1]], 3),
        ([[0]], 0),
        ([[1,1,1],[1,0,1],[0,0,0]], 6),
        ([[1,0,0],[1,0,0]], -1),
        ([[1,1,1],[1,1,1],[0,0,0]], 7),
    ])
def test_minFlips(sut, mat, answer):
    assert answer == sut.minFlips(mat)


@pytest.mark.parametrize('nums, target, answer', [
        ([2,7,11,15], 9, [0, 1]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-3,4,3,90], 0, [0, 2]),
        ([3,2,4], 6, [1, 2]),

    ])
def test_twoSum(sut, nums, target, answer):
    assert answer == sut.twoSum(nums, target)


