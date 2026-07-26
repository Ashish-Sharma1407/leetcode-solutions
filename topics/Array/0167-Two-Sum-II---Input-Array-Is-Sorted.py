############################################################
# Problem  : Two Sum II - Input Array Is Sorted
# ID       : 167
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search
# Runtime  : 0
# Memory   : 20612000
# Language : Python3
# Solved   : 2026-07-26 17:07
# URL      : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
############################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while(start < end):
            if nums[start] + nums[end] == target:
                return [start+1,end+1]
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        return [-1,-1]