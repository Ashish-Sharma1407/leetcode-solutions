############################################################
# Problem  : Search Insert Position
# ID       : 35
# Difficulty: Easy
# Tags     : Array, Binary Search
# Runtime  : 0
# Memory   : 19964000
# Language : Python3
# Solved   : 2026-06-29 21:30
# URL      : https://leetcode.com/problems/search-insert-position/
############################################################
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

                