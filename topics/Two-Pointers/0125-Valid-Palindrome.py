############################################################
# Problem  : Valid Palindrome
# ID       : 125
# Difficulty: Easy
# Tags     : Two Pointers, String
# Runtime  : 21
# Memory   : 19696000
# Language : Python3
# Solved   : 2026-07-26 16:42
# URL      : https://leetcode.com/problems/valid-palindrome/
############################################################
class Solution:
    def alphanumeric(self,s):
        x = ord(s)
        if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""
        s2 = ""
        for ch in s:
            ans = self.alphanumeric(ch)
            if ans:
                s1 += ch
        print(s1)
        for i in range(len(s)-1,-1,-1):
            ans = self.alphanumeric(s[i])
            if ans:
                s2 += s[i]
        return s1 == s2

        