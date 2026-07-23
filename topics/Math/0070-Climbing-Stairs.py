############################################################
# Problem  : Climbing Stairs
# ID       : 70
# Difficulty: Easy
# Tags     : Math, Dynamic Programming, Memoization
# Runtime  : 0
# Memory   : 19240000
# Language : Python3
# Solved   : 2026-07-23 18:38
# URL      : https://leetcode.com/problems/climbing-stairs/
############################################################
class Solution:
    def stairs(self,dp,n):
        if n==1 or n==2:
            return n
        if dp[n]!=-1:
            return dp[n]
        else:
            dp[n] = self.stairs(dp,n-1) + self.stairs(dp,n-2)
            return dp[n]
        
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0]=0
        return self.stairs(dp,n)
        