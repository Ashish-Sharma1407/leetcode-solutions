############################################################
# Problem  : Group Anagrams
# ID       : 49
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Sorting
# Runtime  : 22
# Memory   : 22052000
# Language : Python3
# Solved   : 2026-09-10 21:29
# URL      : https://leetcode.com/problems/group-anagrams/
############################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for val in strs:
            key = "".join(sorted(val))
            dic.update({key:[]})
        for val in strs:
            key = "".join(sorted(val))
            if key in dic:
                dic[key].append(val)
        return list(dic.values())
        