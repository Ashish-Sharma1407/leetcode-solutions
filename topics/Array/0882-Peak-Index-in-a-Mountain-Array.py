############################################################
# Problem  : Peak Index in a Mountain Array
# ID       : 882
# Difficulty: Medium
# Tags     : Array, Binary Search
# Runtime  : 0
# Memory   : 31500000
# Language : Python3
# Solved   : 2026-06-30 08:24
# URL      : https://leetcode.com/problems/peak-index-in-a-mountain-array/
############################################################
class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 2
        ans = len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans
        