############################################################
# Problem  : Container With Most Water
# ID       : 11
# Difficulty: Medium
# Tags     : Array, Two Pointers, Greedy
# Runtime  : 52
# Memory   : 29320000
# Language : Python3
# Solved   : 2026-07-26 17:27
# URL      : https://leetcode.com/problems/container-with-most-water/
############################################################
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_level = 0
        while start < end:
            level = min(height[start],height[end])*(end-start)
            max_level = max(level,max_level)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_level

        