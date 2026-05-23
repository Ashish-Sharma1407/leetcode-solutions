############################################################
# Problem  : Maximum Subarray
# ID       : 53
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Dynamic Programming
# Runtime  : 46
# Memory   : 31488000
# Language : Python3
# Solved   : 2026-05-22 14:45
# URL      : https://leetcode.com/problems/maximum-subarray/
############################################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            currsum = max(nums[i], currsum + nums[i])
            maxsum = max(currsum, maxsum)
        return maxsum
        