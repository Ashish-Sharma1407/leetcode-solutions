############################################################
# Problem  : Length of Last Word
# ID       : 58
# Difficulty: Easy
# Tags     : String
# Runtime  : 0
# Memory   : 19236000
# Language : Python3
# Solved   : 2026-06-22 08:56
# URL      : https://leetcode.com/problems/length-of-last-word/
############################################################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) <= 1:
            return 1
        cnt = -1
        while cnt >= -len(s):
            if s[cnt] == " ":
                return -cnt-1
            cnt -= 1
        return -cnt-1