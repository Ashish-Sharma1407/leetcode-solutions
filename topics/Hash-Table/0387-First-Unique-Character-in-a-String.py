############################################################
# Problem  : First Unique Character in a String
# ID       : 387
# Difficulty: Easy
# Tags     : Hash Table, String, Queue, Counting
# Runtime  : 67
# Memory   : 19528000
# Language : Python3
# Solved   : 2026-09-13 03:57
# URL      : https://leetcode.com/problems/first-unique-character-in-a-string/
############################################################
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic.update({char: 1})
        
        for i, char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1
        