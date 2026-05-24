############################################################
# Problem  : Valid Palindrome
# ID       : 125
# Difficulty: Easy
# Tags     : Two Pointers, String
# Runtime  : 11
# Memory   : 19728000
# Language : Python3
# Solved   : 2026-05-24 13:58
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
        i = 0
        j = len(s)-1

        while i < j:
            if not self.alphanumeric(s[i]):
                i += 1
            elif not self.alphanumeric(s[j]):
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        