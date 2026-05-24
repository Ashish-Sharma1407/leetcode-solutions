############################################################
# Problem  : Reverse String
# ID       : 344
# Difficulty: Easy
# Tags     : Two Pointers, String
# Runtime  : 6
# Memory   : 23516000
# Language : Python3
# Solved   : 2026-05-24 14:03
# URL      : https://leetcode.com/problems/reverse-string/
############################################################
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return s
        