############################################################
# Problem  : Remove Duplicates from Sorted Array
# ID       : 26
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 1
# Memory   : 20204000
# Language : Python3
# Solved   : 2026-11-16 20:00
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
############################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        for i in range(len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start], nums[i] = nums[i], nums[start]
        return start+1
        