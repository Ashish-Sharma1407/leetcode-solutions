############################################################
# Problem  : Substrings of Size Three with Distinct Characters
# ID       : 1987
# Difficulty: Easy
# Tags     : Hash Table, String, Sliding Window, Counting
# Runtime  : 0
# Memory   : 19288000
# Language : Python3
# Solved   : 2026-06-23 14:05
# URL      : https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
############################################################
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        p3 = 2
        cnt = 0
        while p3 != len(s):
            if s[p3]!=s[p3-1] and s[p3-2] != s[p3-1] and s[p3-2] != s[p3]:
                cnt += 1
            p3 += 1
        return cnt