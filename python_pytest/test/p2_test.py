# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = str(self.val)
        if self.next:
            s += "->" + str(self.next)
        return s

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = last = ListNode(0)
        overflow = 0
        while l1 or l2 or overflow:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + overflow
            if val >= 10:
                overflow = 1
                val -= 10
            else:
                overflow = 0
            l = ListNode(val)
            last.next = l
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
            last = l
        return head.next


import pytest

@pytest.fixture
def sut():
    return Solution()

class Test_addTwoNumbers:
    def test_1_and_2(self, sut):
        l1 = ListNode(1)
        l2 = ListNode(2)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "3"

    def test_2_and_3(self, sut):
        l1 = ListNode(2)
        l2 = ListNode(3)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "5"

    def test_5_and_7(self, sut):
        l1 = ListNode(5)
        l2 = ListNode(7)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "2->1"

    def test_0_and_0(self, sut):
        l1 = ListNode(0)
        l2 = ListNode(0)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "0"

    def test_123_and_45(self, sut):
        l1 = ListNode(3)
        l1.next = ListNode(2)
        l1.next.next = ListNode(1)
        l2 = ListNode(5)
        l2.next = ListNode(4)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "8->6->1"

    def test_45_and_123(self, sut):
        l1 = ListNode(5)
        l1.next = ListNode(4)
        l2 = ListNode(3)
        l2.next = ListNode(2)
        l2.next.next = ListNode(1)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "8->6->1"

    def test_12345_and_0(self, sut):
        l1 = ListNode(5)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(2)
        l1.next.next.next.next = ListNode(1)
        l2 = ListNode(0)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "5->4->3->2->1"

    def test_99_and_99(self, sut):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l2 = ListNode(9)
        l2.next = ListNode(9)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "8->9->1"

    def test_99999_and_1(self, sut):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)
        l1.next.next.next = ListNode(9)
        l1.next.next.next.next = ListNode(9)
        l2 = ListNode(1)
        actual = sut.addTwoNumbers(l1, l2)
        assert str(actual) == "0->0->0->0->0->1"
