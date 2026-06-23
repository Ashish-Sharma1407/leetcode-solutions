############################################################
# Problem  : Valid Anagram
# ID       : 242
# Difficulty: Easy
# Tags     : Hash Table, String, Sorting
# Runtime  : 11
# Memory   : 19240000
# Language : Python3
# Solved   : 2026-06-22 11:43
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
            else:
                return False
        
        if all(val == 0 for val in dic.values()):
            return True
        
        return False

