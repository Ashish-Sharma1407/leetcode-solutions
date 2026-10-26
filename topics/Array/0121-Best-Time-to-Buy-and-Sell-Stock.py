############################################################
# Problem  : Best Time to Buy and Sell Stock
# ID       : 121
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Runtime  : 52
# Memory   : 28772000
# Language : Python3
# Solved   : 2026-10-26 19:18
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
############################################################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = prices[i] - buy
                max_profit = max(max_profit, sell)
        return max_profit
        