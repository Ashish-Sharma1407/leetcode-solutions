############################################################
# Problem  : Palindrome Number
# ID       : 9
# Difficulty: Easy
# Tags     : Math
# Runtime  : 14
# Memory   : 19132000
# Language : Python3
# Solved   : 2026-07-17 10:34
# URL      : https://leetcode.com/problems/palindrome-number/
############################################################
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        ans = 0
        while x > 0:
            remainder = x % 10
            ans = (ans * 10) + remainder
            x = x // 10
        if temp == ans:
            return True
        else:
            return False
        
        