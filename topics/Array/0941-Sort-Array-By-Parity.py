############################################################
# Problem  : Sort Array By Parity
# ID       : 941
# Difficulty: Easy
# Tags     : Array, Two Pointers, Sorting
# Runtime  : 0
# Memory   : 19888000
# Language : Python3
# Solved   : 2026-05-21 23:32
# URL      : https://leetcode.com/problems/sort-array-by-parity/
############################################################
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(0,len(nums)):
            if(nums[j] % 2 == 0):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
        return nums