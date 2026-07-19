############################################################
# Problem  : Remove Duplicates from Sorted Array
# ID       : 26
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 0
# Memory   : 20484000
# Language : Python3
# Solved   : 2026-07-19 18:02
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
############################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 0
        while end < len(nums):
            if nums[start] != nums[end]:
                start += 1
                nums[start], nums[end] = nums[end], nums[start]
            end += 1
        return start + 1
        

        