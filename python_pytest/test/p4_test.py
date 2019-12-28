from typing import *
from dataclasses import dataclass

class CombinedList:
    def __init__(self, nums1, nums2):
        assert len(nums1) > 0 and len(nums2) > 0
        if nums1[0] > nums2[0]:
            nums1, nums2 = nums2, nums1
        self.nums1 = nums1
        self.nums2 = nums2

    def __getitem__(self, idx):
        @dataclass
        class Cursor:
            i1: int
            i2: int
            side: int

            def increment(self):
                if self.side == 1:
                    self.i1 += 1
                else:
                    self.i2 += 1

            def flip(self):
                if self.side == 1:
                    self.side = 2
                else:
                    self.side = 1

            def at(self):
                return self.i1 + self.i2 + 1

            def value(self, nums1, nums2):
                return nums1[self.i1] if self.side == 1 else nums2[self.i2]

        cursor = Cursor(0, -1, 1)

        return self.getitem2(idx, cursor)

    def getitem1(self, idx, cursor):
        while cursor.at() < idx:
            print(f"{cursor=}")
            if cursor.side == 1:
                if cursor.i1 == len(self.nums1) - 1:
                    cursor.flip()
                elif cursor.i2 == len(self.nums2) - 1:
                    pass
                elif self.nums1[cursor.i1 + 1] >= self.nums2[cursor.i2 + 1]:
                    cursor.flip()
            else:
                if cursor.i2 == len(self.nums2) - 1:
                    cursor.flip()
                elif cursor.i1 == len(self.nums1) - 1:
                    pass
                elif self.nums2[cursor.i2 + 1] >= self.nums1[cursor.i1 + 1]:
                    cursor.flip()
            cursor.increment()
        print(f"final {cursor=}")
        return cursor.value(self.nums1, self.nums2)

    def getitem2(self, idx, cursor):
        print(f"{cursor=}")
        l = 0
        h = len(self.nums1)
        while True:
            last = l, h
            cursor.i1 = int((h + l) / 2)
            cursor.i2 = idx - cursor.i1 - 1
            if cursor.i2 < -1:
                h = h - int((h - l) / 2)
                continue
            if cursor.i2 > len(self.nums2) - 1:
                l = l + int((h - l) / 2)
                continue
            print(f"{h,l=}, {cursor=}, {last=}")
            if cursor.side == 1:
                prec = self.nums2[cursor.i2] if cursor.i2 >= 0 else cursor.value(self.nums1, self.nums2) - 1
                post = self.nums2[cursor.i2 + 1] if cursor.i2 < len(self.nums2) - 1 else cursor.value(self.nums1, self.nums2) + 1
                valid = prec <= cursor.value(self.nums1, self.nums2) <= post
            else:
                prec = self.nums1[cursor.i1] if cursor.i1 >= 0 else cursor.value(self.nums1, self.nums2) - 1
                post = self.nums1[cursor.i1 + 1] if cursor.i1 < len(self.nums1) - 1 else cursor.value(self.nums1, self.nums2) + 1
                valid = prec <= cursor.value(self.nums1, self.nums2) <= post
            if valid:
                break

            cursor.flip()
            if cursor.side == 1:
                prec = self.nums2[cursor.i2] if cursor.i2 >= 0 else cursor.value(self.nums1, self.nums2) - 1
                post = self.nums2[cursor.i2 + 1] if cursor.i2 < len(self.nums2) - 1 else cursor.value(self.nums1, self.nums2) + 1
                valid = prec <= cursor.value(self.nums1, self.nums2) <= post
            else:
                prec = self.nums1[cursor.i1] if cursor.i1 >= 0 else cursor.value(self.nums1, self.nums2) - 1
                post = self.nums1[cursor.i1 + 1] if cursor.i1 < len(self.nums1) - 1 else cursor.value(self.nums1, self.nums2) + 1
                valid = prec <= cursor.value(self.nums1, self.nums2) <= post
            if valid:
                break

            if cursor.i2 >= 0 and self.nums1[cursor.i1] <= self.nums2[cursor.i2]:
                l = l + int((h - l) / 2)
            else:
                h = h - int((h - l) / 2)
            assert last != (l, h)

            cursor.flip()

        print(f"final {cursor=}")
        return cursor.value(self.nums1, self.nums2)

    def __len__(self):
        return len(self.nums1) + len(self.nums2)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = CombinedList(nums1, nums2)
        if len(comb) % 2 == 0:
            return (comb[int(len(comb) / 2) - 1] + comb[int(len(comb) / 2)]) / 2
        else:
            return comb[int(len(comb) / 2)]


import pytest

@pytest.fixture
def sut():
    return Solution()


class TestCombinedList:
    def test_1つずつ(self):
        sut = CombinedList([1], [2])
        assert len(sut) == 2
        assert sut[0] == 1
        assert sut[1] == 2

    def test_単純(self):
        sut = CombinedList([1,3,5], [2,4,6])
        assert len(sut) == 6
        assert sut[0] == 1
        assert sut[1] == 2
        assert sut[2] == 3
        assert sut[3] == 4
        assert sut[4] == 5
        assert sut[5] == 6

    def test_単純_奇数個(self):
        sut = CombinedList([1,3,5,7], [2,4,6])
        assert len(sut) == 7
        assert sut[0] == 1
        assert sut[1] == 2
        assert sut[2] == 3
        assert sut[3] == 4
        assert sut[4] == 5
        assert sut[5] == 6
        assert sut[6] == 7

    def test_単純_奇数個_2(self):
        sut = CombinedList([1,3,5], [2,4,6,8])
        assert len(sut) == 7
        assert sut[0] == 1
        assert sut[1] == 2
        assert sut[2] == 3
        assert sut[3] == 4
        assert sut[4] == 5
        assert sut[5] == 6
        assert sut[6] == 8

    def test_かたより(self):
        sut = CombinedList([1,2,3], [4,5,6])
        assert len(sut) == 6
        assert sut[0] == 1
        assert sut[1] == 2
        assert sut[2] == 3
        assert sut[3] == 4
        assert sut[4] == 5
        assert sut[5] == 6

def test_nが1でmが1(sut):
    assert sut.findMedianSortedArrays([1], [3]) == 2

def test_nが3でmが4(sut):
    assert sut.findMedianSortedArrays([1,3,5], [2,4,6,8]) == 4

def test_nが4でmが3(sut):
    assert sut.findMedianSortedArrays([1,3,5,7], [2,4,6]) == 4

def test_中央値が1つ(sut):
    assert sut.findMedianSortedArrays([1,3,5,7], [2,4,6]) == 4

def test_中央値が2つの平均(sut):
    assert sut.findMedianSortedArrays([1,3,5], [2,4,6]) == 3.5

def test_中央値が2つの平均_整数(sut):
    assert sut.findMedianSortedArrays([1,3,10], [2,3,9]) == 3

def test_中央値が2つの平均_小数部あり(sut):
    assert sut.findMedianSortedArrays([1,3,5,7], [2,4,6,8]) == 4.5

def test_nが1(sut):
    assert sut.findMedianSortedArrays([4], [1,3,9]) == 3.5

def test_mが1(sut):
    assert sut.findMedianSortedArrays([4,8,9], [1]) == 6

def test_nums1の最大値がnums2の最小値未満_中央値はnums1(sut):
    assert sut.findMedianSortedArrays([1,2,3,4,5], [6,7]) == 4

def test_nums1の最大値がnums2の最小値未満_中央値はnums2(sut):
    assert sut.findMedianSortedArrays([1,2,3], [4,5,6,7]) == 4

def test_nums1の最小値がnums2の最大値より大きい_中央値はnum1(sut):
    assert sut.findMedianSortedArrays([4,5,6,7], [1,2,3]) == 4

def test_nums1の最小値がnums2の最大値より大きい_中央値はnum2(sut):
    assert sut.findMedianSortedArrays([6,7], [1,2,3,4,5]) == 4

def test_nとmがとても大きい(sut):
    assert sut.findMedianSortedArrays(
            list(range(0, 100000, 2)),
            list(range(1, 100000, 2))) == 49999.5

def test_nums1とnums2はすべて同じ数値(sut):
    assert sut.findMedianSortedArrays([1] * 10000, [1] * 10000) == 1


