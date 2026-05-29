############################################################
# Problem  : Find All Numbers Disappeared in an Array
# ID       : 448
# Difficulty: Easy
# Tags     : Array, Hash Table
# Runtime  : 26
# Memory   : 30204000
# Language : Python3
# Solved   : 2026-05-29 20:30
# URL      : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
############################################################
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for val in nums:
            if val not in s:
                s.add(val)
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans