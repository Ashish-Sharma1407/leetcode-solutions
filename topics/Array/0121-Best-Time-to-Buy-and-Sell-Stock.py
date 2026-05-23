############################################################
# Problem  : Best Time to Buy and Sell Stock
# ID       : 121
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Runtime  : 38
# Memory   : 28732000
# Language : Python3
# Solved   : 2026-05-22 17:22
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
############################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif (prices[i] - buy) > sell:
                sell = prices[i] - buy
        return sell
        