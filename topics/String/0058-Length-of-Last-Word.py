############################################################
# Problem  : Length of Last Word
# ID       : 58
# Difficulty: Easy
# Tags     : String
# Runtime  : 0
# Memory   : 19316000
# Language : Python3
# Solved   : 2026-05-24 14:35
# URL      : https://leetcode.com/problems/length-of-last-word/
############################################################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) <= 1:
            return 1
        size = 0
        ptr = len(s)-1
        while ptr >= 0:
            if s[ptr] == " ":
                break
            else:
                size += 1
                ptr -= 1
        return size

        