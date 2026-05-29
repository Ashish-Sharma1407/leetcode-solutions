############################################################
# Problem  : Valid Anagram
# ID       : 242
# Difficulty: Easy
# Tags     : Hash Table, String, Sorting
# Runtime  : 20
# Memory   : 20296000
# Language : Python3
# Solved   : 2026-05-29 12:11
# URL      : https://leetcode.com/problems/valid-anagram/
############################################################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1, l2 = list(s), list(t)
        l1.sort()
        l2.sort()
        l1 = "".join(l1)
        l2 = "".join(l2)
        if l1 == l2:
            return True
        else:
            return False
        