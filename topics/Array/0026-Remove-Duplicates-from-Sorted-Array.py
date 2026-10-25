############################################################
# Problem  : Remove Duplicates from Sorted Array
# ID       : 26
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 0
# Memory   : 20444000
# Language : Python3
# Solved   : 2026-10-25 19:48
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
############################################################
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i+1
        