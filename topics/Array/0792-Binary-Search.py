############################################################
# Problem  : Binary Search
# ID       : 792
# Difficulty: Easy
# Tags     : Array, Binary Search
# Runtime  : 0
# Memory   : 20540000
# Language : Python3
# Solved   : 2026-06-29 20:52
# URL      : https://leetcode.com/problems/binary-search/
############################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low)// 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1