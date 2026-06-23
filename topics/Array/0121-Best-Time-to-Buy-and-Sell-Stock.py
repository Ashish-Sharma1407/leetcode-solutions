############################################################
# Problem  : Best Time to Buy and Sell Stock
# ID       : 121
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Runtime  : 55
# Memory   : 28552000
# Language : Python3
# Solved   : 2026-06-19 11:12
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
############################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = max(sell, prices[i]-buy)
        return sell
        