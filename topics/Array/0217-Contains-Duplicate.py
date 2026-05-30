############################################################
# Problem  : Contains Duplicate
# ID       : 217
# Difficulty: Easy
# Tags     : Array, Hash Table, Sorting
# Runtime  : 8
# Memory   : 31400000
# Language : Python3
# Solved   : 2026-05-30 17:11
# URL      : https://leetcode.com/problems/contains-duplicate/
############################################################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for val in nums:
            if val in s:
                return True
            else:
                s.add(val)
        return False