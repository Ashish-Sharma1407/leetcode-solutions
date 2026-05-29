############################################################
# Problem  : Valid Anagram
# ID       : 242
# Difficulty: Easy
# Tags     : Hash Table, String, Sorting
# Runtime  : 15
# Memory   : 19388000
# Language : Python3
# Solved   : 2026-05-29 12:23
# URL      : https://leetcode.com/problems/valid-anagram/
############################################################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic.update({s[i]:1})

        for i in range(len(t)):
            if t[i] in dic:
                dic[t[i]] -= 1
        
        if all(value == 0 for value in dic.values()):
            return True
        else:
            return False



        