############################################################
# Problem  : Sort Colors
# ID       : 75
# Difficulty: Medium
# Tags     : Array, Two Pointers, Sorting
# Runtime  : 0
# Memory   : 19324000
# Language : Python3
# Solved   : 2026-06-29 19:19
# URL      : https://leetcode.com/problems/sort-colors/
############################################################
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 1:
                i += 1

            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1

            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
        
        return nums 

        