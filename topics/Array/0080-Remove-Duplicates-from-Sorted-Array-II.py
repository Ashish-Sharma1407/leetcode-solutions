############################################################
# Problem  : Remove Duplicates from Sorted Array II
# ID       : 80
# Difficulty: Medium
# Tags     : Array, Two Pointers
# Runtime  : 79
# Memory   : 21804000
# Language : Python3
# Solved   : 2026-09-10 19:49
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
############################################################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        start = 1
        for i in range(2,len(nums)):
            if nums[i] != nums[start-1]:
                start += 1
                nums[start], nums[i] = nums[i], nums[start]
        return start + 1

        