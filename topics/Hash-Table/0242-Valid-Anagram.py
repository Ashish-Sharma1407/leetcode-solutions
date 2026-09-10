############################################################
# Problem  : Valid Anagram
# ID       : 242
# Difficulty: Easy
# Tags     : Hash Table, String, Sorting
# Runtime  : 12
# Memory   : 19456000
# Language : Python3
# Solved   : 2026-09-10 21:21
# URL      : https://leetcode.com/problems/valid-anagram/
############################################################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic.update({char: 1})
        for char in t:
            if char in dic:
                dic[char] -= 1
        for value in dic.values():
            if value != 0:
                return False
        return True
        