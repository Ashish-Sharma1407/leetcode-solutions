############################################################
# Problem  : Richest Customer Wealth
# ID       : 1791
# Difficulty: Easy
# Tags     : Array, Matrix
# Runtime  : 0
# Memory   : 19328000
# Language : Python3
# Solved   : 2026-09-10 20:17
# URL      : https://leetcode.com/problems/richest-customer-wealth/
############################################################
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for account in accounts:
            ans = max(ans,sum(account))
        return ans