############################################################
# Problem  : Two Sum
# ID       : 1
# Difficulty: Easy
# Tags     : Array, Hash Table
# Runtime  : 4
# Memory   : 20516000
# Language : Python3
# Solved   : 2026-05-24 12:22
# URL      : https://leetcode.com/problems/two-sum/
############################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in mp:
                return [mp[diff], i]

            mp[nums[i]] = i