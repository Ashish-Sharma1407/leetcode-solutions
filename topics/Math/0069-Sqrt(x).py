############################################################
# Problem  : Sqrt(x)
# ID       : 69
# Difficulty: Easy
# Tags     : Math, Binary Search
# Runtime  : 3
# Memory   : 19224000
# Language : Python3
# Solved   : 2026-06-30 09:29
# URL      : https://leetcode.com/problems/sqrtx/
############################################################
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0
        while l <= r:
            mid = l + (r - l)//2
            if mid*mid > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans