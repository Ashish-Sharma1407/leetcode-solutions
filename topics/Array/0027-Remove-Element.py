############################################################
# Problem  : Remove Element
# ID       : 27
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Runtime  : 0
# Memory   : 12260000
# Language : Python
# Solved   : 2026-11-19 20:06
# URL      : https://leetcode.com/problems/remove-element/
############################################################
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k