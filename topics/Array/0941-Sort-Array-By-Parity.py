############################################################
# Problem  : Sort Array By Parity
# ID       : 941
# Difficulty: Easy
# Tags     : Array, Two Pointers, Sorting
# Runtime  : 0
# Memory   : 19748000
# Language : Python3
# Solved   : 2026-06-19 10:04
# URL      : https://leetcode.com/problems/sort-array-by-parity/
############################################################
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums