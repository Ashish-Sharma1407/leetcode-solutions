############################################################
# Problem  : Best Time to Buy and Sell Stock II
# ID       : 122
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# Runtime  : 3
# Memory   : 20392000
# Language : Python3
# Solved   : 2026-05-22 17:38
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
############################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                sell += prices[i]-buy
                buy = prices[i]
        return sell