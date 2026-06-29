############################################################
# Problem  : Non-overlapping Intervals
# ID       : 435
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy, Sorting
# Runtime  : 59
# Memory   : 49032000
# Language : Python3
# Solved   : 2026-06-29 20:29
# URL      : https://leetcode.com/problems/non-overlapping-intervals/
############################################################
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 1
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                count += 1
                prev = i
        return len(intervals)-count