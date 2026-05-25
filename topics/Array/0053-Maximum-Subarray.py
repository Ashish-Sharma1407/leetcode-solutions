############################################################
# Problem  : Maximum Subarray
# ID       : 53
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Dynamic Programming
# Runtime  : 47
# Memory   : 31228000
# Language : Python3
# Solved   : 2026-05-25 14:03
# URL      : https://leetcode.com/problems/maximum-subarray/
############################################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = nums[0]
        ms = nums[0]
        for i in range(1,len(nums)):
            cs = max(nums[i], cs + nums[i])
            ms = max(cs, ms)
        return ms
        