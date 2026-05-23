############################################################
# Problem  : Maximum Subarray
# ID       : 53
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Dynamic Programming
# Runtime  : 90
# Memory   : 32952000
# Language : Python3
# Solved   : 2025-11-15 20:12
# URL      : https://leetcode.com/problems/maximum-subarray/
############################################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range (1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum