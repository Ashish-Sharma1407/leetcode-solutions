############################################################
# Problem  : Running Sum of 1d Array
# ID       : 1603
# Difficulty: Easy
# Tags     : Array, Prefix Sum
# Runtime  : 0
# Memory   : 19340000
# Language : Python3
# Solved   : 2026-05-21 22:08
# URL      : https://leetcode.com/problems/running-sum-of-1d-array/
############################################################
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            nums[i] = add
        return nums
        