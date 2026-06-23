############################################################
# Problem  : Richest Customer Wealth
# ID       : 1791
# Difficulty: Easy
# Tags     : Array, Matrix
# Runtime  : 0
# Memory   : 19292000
# Language : Python3
# Solved   : 2026-06-19 12:11
# URL      : https://leetcode.com/problems/richest-customer-wealth/
############################################################
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            max_wealth = max(max_wealth, sum(accounts[i]))
        return max_wealth
        