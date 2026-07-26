############################################################
# Problem  : Merge Strings Alternately
# ID       : 1894
# Difficulty: Easy
# Tags     : Two Pointers, String
# Runtime  : 43
# Memory   : 19204000
# Language : Python3
# Solved   : 2026-07-26 16:32
# URL      : https://leetcode.com/problems/merge-strings-alternately/
############################################################
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        l = []
        while i < len(word1) and j < len(word2):
            l.append(word1[i])
            l.append(word2[j])
            i+=1
            j+=1
        l.extend(word1[i:])
        l.extend(word2[j:])
        return "".join(l)