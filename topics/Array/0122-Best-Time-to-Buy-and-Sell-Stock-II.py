############################################################
# Problem  : Best Time to Buy and Sell Stock II
# ID       : 122
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# Runtime  : 1
# Memory   : 20388000
# Language : Python3
# Solved   : 2026-09-10 20:11
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
############################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = prices[i] - buy
                total_profit += sell
                buy = prices[i]
                sell = 0
        return total_profit