############################################################
# Problem  : Intersection of Two Arrays
# ID       : 349
# Difficulty: Easy
# Tags     : Array, Hash Table, Two Pointers, Binary Search, Sorting
# Runtime  : 0
# Memory   : 19248000
# Language : Python3
# Solved   : 2026-09-10 20:56
# URL      : https://leetcode.com/problems/intersection-of-two-arrays/
############################################################
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

        