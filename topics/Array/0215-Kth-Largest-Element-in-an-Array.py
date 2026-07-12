############################################################
# Problem  : Kth Largest Element in an Array
# ID       : 215
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
# Runtime  : 252
# Memory   : 35004000
# Language : Python3
# Solved   : 2026-07-12 08:02
# URL      : https://leetcode.com/problems/kth-largest-element-in-an-array/
############################################################
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h,num)
        return heapq.nlargest(k,h)[-1]
        