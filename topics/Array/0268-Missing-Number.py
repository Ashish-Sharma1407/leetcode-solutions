############################################################
# Problem  : Missing Number
# ID       : 268
# Difficulty: Easy
# Tags     : Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
# Runtime  : 3
# Memory   : 20568000
# Language : Python3
# Solved   : 2026-05-26 14:38
# URL      : https://leetcode.com/problems/missing-number/
############################################################
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        actualsum = num * (num + 1) / 2
        numssum= 0 
        for i in range(num):
            numssum += nums[i]
        return int(actualsum-numssum)