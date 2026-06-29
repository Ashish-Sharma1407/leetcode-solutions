############################################################
# Problem  : Merge Sorted Array
# ID       : 88
# Difficulty: Easy
# Tags     : Array, Two Pointers, Sorting
# Runtime  : 0
# Memory   : 19292000
# Language : Python3
# Solved   : 2026-06-29 19:43
# URL      : https://leetcode.com/problems/merge-sorted-array/
############################################################
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i < 0 or nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1 
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
                
        