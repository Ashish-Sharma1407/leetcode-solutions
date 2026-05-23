############################################################
# Problem  : Remove Duplicates from Sorted Array II
# ID       : 80
# Difficulty: Medium
# Tags     : Array, Two Pointers
# Runtime  : 86
# Memory   : 22460000
# Language : Python3
# Solved   : 2026-05-21 23:14
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
############################################################
class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 1
        for j in range(2, len(arr)):
            if (arr[j] != arr[i-1]):
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        return i+1
        