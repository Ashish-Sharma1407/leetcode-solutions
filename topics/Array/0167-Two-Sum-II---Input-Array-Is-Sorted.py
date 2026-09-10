############################################################
# Problem  : Two Sum II - Input Array Is Sorted
# ID       : 167
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search
# Runtime  : 7
# Memory   : 22488000
# Language : Python3
# Solved   : 2026-09-10 20:52
# URL      : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
############################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return [-1,-1]
        

        