############################################################
# Problem  : House Robber
# ID       : 198
# Difficulty: Medium
# Tags     : Array, Dynamic Programming
# Runtime  : 0
# Memory   : 19348000
# Language : Python3
# Solved   : 2026-07-23 20:24
# URL      : https://leetcode.com/problems/house-robber/
############################################################
class Solution:
    def steal(self,i,nums,dp):
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        take = nums[i] + self.steal(i+2,nums,dp)
        not_take = self.steal(i+1,nums,dp)
        dp[i] = max(take,not_take)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.steal(0,nums,dp)

        