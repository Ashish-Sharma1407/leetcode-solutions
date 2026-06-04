############################################################
# Problem  : Missing Number
# ID       : 268
# Difficulty: Easy
# Tags     : Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
# Runtime  : 3
# Memory   : 20292000
# Language : Python3
# Solved   : 2026-06-04 20:26
# URL      : https://leetcode.com/problems/missing-number/
############################################################
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (int(len(nums)*(len(nums)+1)/2) - sum(nums))
        