############################################################
# Problem  : Find the Index of the First Occurrence in a String
# ID       : 28
# Difficulty: Easy
# Tags     : Two Pointers, String, String Matching
# Runtime  : 0
# Memory   : 19140000
# Language : Python3
# Solved   : 2026-07-21 14:42
# URL      : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
############################################################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)