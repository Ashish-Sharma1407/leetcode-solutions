############################################################
# Problem  : First Unique Character in a String
# ID       : 387
# Difficulty: Easy
# Tags     : Hash Table, String, Queue, Counting
# Runtime  : 89
# Memory   : 19636000
# Language : Python3
# Solved   : 2026-05-28 16:55
# URL      : https://leetcode.com/problems/first-unique-character-in-a-string/
############################################################
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic.update({s[i]:1})

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i

        return -1
        