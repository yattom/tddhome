from typing import *
import math
import random

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for v in arr:
            if v * 2 in s or v / 2 in s:
                return True
            s.add(v)
        return False

    def minSteps(self, s: str, t: str) -> int:
        s_map = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        for c in s:
            s_map[c] += 1

        for c in t:
            s_map[c] -= 1

        return int(sum([abs(v) for v in s_map.values()]) / 2)

import bisect
class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 60 * 60
        elif freq == 'day':
            delta = 60 * 60 * 24
        else:
            raise ValueError('freq')

        tweets = self.tweets[tweetName] if tweetName in self.tweets else []

        last = bisect.bisect_left(tweets, startTime)
        result = []
        for i in range((endTime - startTime) // delta + 1):
            delta_end = startTime + (i + 1) * delta
            end = bisect.bisect_left(tweets, delta_end)
            result.append(end - last)
            last = end
        return result


import pytest

@pytest.fixture
def sut():
    return Solution()


class TestTweetCounts:
    def test_zero(self):
        sut = TweetCounts()
        assert sut.getTweetCountsPerFrequency('day', 'tweet3', 0, 210) == [0]

    def test_example(self):
        sut = TweetCounts()
        sut.recordTweet("tweet3",0)
        sut.recordTweet( "tweet3",60)
        sut.recordTweet( "tweet3",10)
        assert [2] == sut.getTweetCountsPerFrequency( "minute","tweet3",0,59)
        assert [2,1] == sut.getTweetCountsPerFrequency( "minute","tweet3",0,60)
        sut.recordTweet( "tweet3",120)
        assert [4] == sut.getTweetCountsPerFrequency( "hour","tweet3",0,210)
        assert [4] + [0] * 24 == sut.getTweetCountsPerFrequency( "hour","tweet3",0,60*60*24)
        assert [4, 0] == sut.getTweetCountsPerFrequency( "day","tweet3",0,60*60*24)
        assert [2] == sut.getTweetCountsPerFrequency( "day","tweet3",11,60*60*24)


def test_tweetFreq_1():
    cmds = ["TweetCounts","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet"],
    args = [[],["tweet0",99],["tweet1",80],["tweet2",29],["tweet3",81],["tweet4",56],["day","tweet4",56,2667],["tweet1",56],["tweet0",96],["tweet4",35],["tweet1",51],["tweet2",45],["tweet0",74],["tweet1",63]],
    answers = [None,None,None,None,None,None,[1],None,None,None,None,None,None,None],

    for i in range(len(cmds)):
        c = cmds[i]
        a = args[i]
        ans = answers[i]

        if c == "TweetCounts":
            sut = TweetCount()
            assert ans == None
        elif c == "recordTweet":
            sut.recordTweet(*a)
            assert ans == None
        elif c == "getTweetCountsPerFrequency":
            assert ans == sut.getTweetCountsPerFrequency(*a)



def test_checkIfExist(sut, arr, answer):
    assert answer == sut.checkIfExist(arr)

@pytest.mark.parametrize("arr,answer", [
    ([10,2,5,3], True),
    ([2,5,3,10], True),
    ([7,1,14,11], True),
    ([3,1,7,11], False),
])
def test_checkIfExist(sut, arr, answer):
    assert answer == sut.checkIfExist(arr)


@pytest.mark.parametrize("s,t,answer", [
    ("abc", "cab", 0),
    ("abc", "aaa", 2),
    ("aac", "aaa", 1),
    ("leetcode", "practice", 5),
    ("anagram", "mangaar", 0),
    ("xxyyzz", "xxyyzz", 0),
    ("friend", "family", 4),
])
def test_minSteps(sut, s, t, answer):
    assert answer == sut.minSteps(s, t)


