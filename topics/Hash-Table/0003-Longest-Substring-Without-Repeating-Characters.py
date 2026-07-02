############################################################
# Problem  : Longest Substring Without Repeating Characters
# ID       : 3
# Difficulty: Medium
# Tags     : Hash Table, String, Sliding Window
# Runtime  : 11
# Memory   : 19216000
# Language : Python3
# Solved   : 2026-07-02 15:09
# URL      : https://leetcode.com/problems/longest-substring-without-repeating-characters/
############################################################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        sets = set({})
        
        ans = 1
        sets.add(s[0])
        i = 0
        j = 1
        
        while j < len(s):
            while s[j] in sets:
                sets.discard(s[i])
                i += 1
            sets.add(s[j])
            j += 1
            ans = max(ans, j-i)
        return ans