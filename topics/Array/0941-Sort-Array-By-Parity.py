############################################################
# Problem  : Sort Array By Parity
# ID       : 941
# Difficulty: Easy
# Tags     : Array, Two Pointers, Sorting
# Runtime  : 2
# Memory   : 19744000
# Language : Python3
# Solved   : 2026-09-10 19:55
# URL      : https://leetcode.com/problems/sort-array-by-parity/
############################################################
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        start = 0
        for i in range(0,len(nums)):
            if nums[i] % 2 == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start+=1
        return nums
        