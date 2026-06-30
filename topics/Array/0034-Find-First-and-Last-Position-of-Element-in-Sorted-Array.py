############################################################
# Problem  : Find First and Last Position of Element in Sorted Array
# ID       : 34
# Difficulty: Medium
# Tags     : Array, Binary Search
# Runtime  : 0
# Memory   : 20564000
# Language : Python3
# Solved   : 2026-06-30 07:56
# URL      : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
############################################################
class Solution:
    def lowerBound(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def upperBound(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums,target)
        ub = self.upperBound(nums,target)
        if lb == ub:
            return [-1,-1]
        else:
            return [lb,ub-1]
        