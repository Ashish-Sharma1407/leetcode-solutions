############################################################
# Problem  : Two Sum II - Input Array Is Sorted
# ID       : 167
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search
# Runtime  : 10
# Memory   : 20512000
# Language : Python3
# Solved   : 2026-05-28 16:45
# URL      : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
############################################################
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0
        end = len(numbers)-1
        while st < end:
            if (numbers[st] + numbers[end]) == target:
                return [st+1,end+1]
            elif (numbers[st] + numbers[end]) < target:
                st += 1
            elif (numbers[st] + numbers[end]) > target:
                end -= 1
        return [-1,-1]
        