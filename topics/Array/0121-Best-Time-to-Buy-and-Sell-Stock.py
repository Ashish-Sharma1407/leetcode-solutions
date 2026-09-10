############################################################
# Problem  : Best Time to Buy and Sell Stock
# ID       : 121
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Runtime  : 42
# Memory   : 28224000
# Language : Python3
# Solved   : 2026-09-10 20:06
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
############################################################
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buy = nums[0]
        sell = 0
        mp = 0
        for i in range(1, len(nums)):
            if nums[i] < buy:
                buy = nums[i]
            else:
                sell = nums[i] - buy
                mp = max(mp,sell)
        return mp