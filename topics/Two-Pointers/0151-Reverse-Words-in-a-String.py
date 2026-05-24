############################################################
# Problem  : Reverse Words in a String
# ID       : 151
# Difficulty: Medium
# Tags     : Two Pointers, String
# Runtime  : 0
# Memory   : 19264000
# Language : Python3
# Solved   : 2026-05-24 14:08
# URL      : https://leetcode.com/problems/reverse-words-in-a-string/
############################################################
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s.reverse()
        return " ".join(s)

        