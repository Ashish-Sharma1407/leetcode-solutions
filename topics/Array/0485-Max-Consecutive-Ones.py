############################################################
# Problem  : Max Consecutive Ones
# ID       : 485
# Difficulty: Easy
# Tags     : Array
# Runtime  : 21
# Memory   : 22008000
# Language : Python3
# Solved   : 2026-05-29 19:18
# URL      : https://leetcode.com/problems/max-consecutive-ones/
############################################################
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        ans = 0
        for val in nums:
            if val == 1:
                counter += 1
                ans = max(ans,counter)
            elif val == 0:
                counter = 0
        return ans
        