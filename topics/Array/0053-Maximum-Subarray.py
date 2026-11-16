############################################################
# Problem  : Maximum Subarray
# ID       : 53
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Dynamic Programming
# Runtime  : 42
# Memory   : 31100000
# Language : Python3
# Solved   : 2026-10-29 18:28
# URL      : https://leetcode.com/problems/maximum-subarray/
############################################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        cs = nums[0]
        for i in range(1, len(nums)):
            cs = max(nums[i],cs+nums[i])
            ms = max(ms,cs)
        return ms
        