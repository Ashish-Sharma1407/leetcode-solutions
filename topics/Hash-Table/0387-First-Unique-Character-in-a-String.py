############################################################
# Problem  : First Unique Character in a String
# ID       : 387
# Difficulty: Easy
# Tags     : Hash Table, String, Queue, Counting
# Runtime  : 64
# Memory   : 19580000
# Language : Python3
# Solved   : 2026-06-22 10:54
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
        
        ans = ""
        for key in dic.keys():
            if dic[key] == 1:
                ans += key
                break
        
        for i in range(len(s)):
            if s[i] == ans:
                return i
        
        return -1