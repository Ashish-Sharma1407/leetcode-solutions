############################################################
# Problem  : Substrings of Size Three with Distinct Characters
# ID       : 1987
# Difficulty: Easy
# Tags     : Hash Table, String, Sliding Window, Counting
# Runtime  : 0
# Memory   : 19344000
# Language : Python3
# Solved   : 2026-09-10 21:33
# URL      : https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
############################################################
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        nxt = 2
        cnt = 0
        while nxt < len(s):
            if s[prev] != s[curr] and s[prev] != s[nxt] and s[curr] != s[nxt]:
                cnt += 1
            prev += 1
            curr += 1
            nxt += 1
        return cnt