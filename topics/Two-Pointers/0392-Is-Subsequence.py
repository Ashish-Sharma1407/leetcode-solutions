############################################################
# Problem  : Is Subsequence
# ID       : 392
# Difficulty: Easy
# Tags     : Two Pointers, String, Dynamic Programming
# Runtime  : 3
# Memory   : 19208000
# Language : Python3
# Solved   : 2026-07-26 17:03
# URL      : https://leetcode.com/problems/is-subsequence/
############################################################
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i +=1
        return i == len(s)

        