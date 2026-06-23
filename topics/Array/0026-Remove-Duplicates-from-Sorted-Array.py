############################################################
# Problem  : Remove Duplicates from Sorted Array
# ID       : 26
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 0
# Memory   : 20448000
# Language : Python3
# Solved   : 2026-06-19 09:44
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
############################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = 1
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        return i+1

        