############################################################
# Problem  : Best Time to Buy and Sell Stock
# ID       : 121
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Runtime  : 47
# Memory   : 28652000
# Language : Python3
# Solved   : 2026-07-20 09:24
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
############################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                sell = prices[i] - buy
                maxprofit = max(sell, maxprofit)
        return maxprofit