############################################################
# Problem  : Intersection of Two Arrays
# ID       : 349
# Difficulty: Easy
# Tags     : Array, Hash Table, Two Pointers, Binary Search, Sorting
# Runtime  : 0
# Memory   : 19360000
# Language : Python3
# Solved   : 2026-06-22 10:21
# URL      : https://leetcode.com/problems/intersection-of-two-arrays/
############################################################
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return list(set1.intersection(set2))

        