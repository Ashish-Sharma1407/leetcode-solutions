############################################################
# Problem  : Move Zeroes
# ID       : 283
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 7
# Memory   : 20420000
# Language : Python3
# Solved   : 2026-06-04 11:32
# URL      : https://leetcode.com/problems/move-zeroes/
############################################################
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        if i == len(nums):
            return
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1