############################################################
# Problem  : Remove Duplicates from Sorted Array II
# ID       : 80
# Difficulty: Medium
# Tags     : Array, Two Pointers
# Runtime  : 82
# Memory   : 22372000
# Language : Python3
# Solved   : 2026-07-25 17:50
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
        