############################################################
# Problem  : Two Sum
# ID       : 1
# Difficulty: Easy
# Tags     : Array, Hash Table
# Runtime  : 2
# Memory   : 20304000
# Language : Python3
# Solved   : 2026-10-23 09:55
# URL      : https://leetcode.com/problems/two-sum/
############################################################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [dic[target-nums[i]], i]
            else:
                dic.update({nums[i]: i})

        