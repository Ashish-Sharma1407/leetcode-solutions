############################################################
# Problem  : Group Anagrams
# ID       : 49
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Sorting
# Runtime  : 15
# Memory   : 22128000
# Language : Python3
# Solved   : 2026-05-30 20:43
# URL      : https://leetcode.com/problems/group-anagrams/
############################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            key = "".join(sorted(word))
            dic[key] = []
        for word in strs:
            key = "".join(sorted(word))
            if key in dic:
                dic[key].append(word)
        return list(dic.values())