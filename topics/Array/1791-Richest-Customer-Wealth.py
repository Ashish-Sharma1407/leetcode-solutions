############################################################
# Problem  : Richest Customer Wealth
# ID       : 1791
# Difficulty: Easy
# Tags     : Array, Matrix
# Runtime  : 0
# Memory   : 19532000
# Language : Python3
# Solved   : 2026-05-22 17:51
# URL      : https://leetcode.com/problems/richest-customer-wealth/
############################################################
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            ans = max(sum(accounts[i]),ans)
        return ans
        