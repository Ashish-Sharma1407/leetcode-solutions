############################################################
# Problem  : Remove Duplicates from Sorted Array
# ID       : 26
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 0
# Memory   : 20436000
# Language : Python3
# Solved   : 2026-09-10 19:35
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
############################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                start += 1
                nums[start],nums[i] = nums[i],nums[start]
        return start + 1
        