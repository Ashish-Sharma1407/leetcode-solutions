############################################################
# Problem  : Maximum Average Subarray I
# ID       : 643
# Difficulty: Easy
# Tags     : Array, Sliding Window
# Runtime  : 69
# Memory   : 29472000
# Language : Python3
# Solved   : 2026-11-18 20:43
# URL      : https://leetcode.com/problems/maximum-average-subarray-i/
############################################################
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum = window
        start = 0
        end = k
        while end < len(nums):
            window += nums[end] - nums[start]
            max_sum = max(max_sum, window)
            start += 1
            end += 1
        return max_sum / k