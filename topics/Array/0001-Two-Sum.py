############################################################
# Problem  : Two Sum
# ID       : 1
# Difficulty: Easy
# Tags     : Array, Hash Table
# Runtime  : 0
# Memory   : 20320000
# Language : Python3
# Solved   : 2026-07-16 18:50
# URL      : https://leetcode.com/problems/two-sum/
############################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return[dic[target - nums[i]], i]
            else:
                dic.update({nums[i]: i})
        return[-1,-1]

        