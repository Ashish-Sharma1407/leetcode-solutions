############################################################
# Problem  : Max Consecutive Ones
# ID       : 485
# Difficulty: Easy
# Tags     : Array
# Runtime  : 21
# Memory   : 21824000
# Language : Python3
# Solved   : 2026-06-04 20:41
# URL      : https://leetcode.com/problems/max-consecutive-ones/
############################################################
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for val in nums:
            if val == 1:
                count += 1
                ans = max(ans, count)
            if val == 0:
                count = 0
        return ans