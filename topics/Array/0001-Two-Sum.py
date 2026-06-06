############################################################
# Problem  : Two Sum
# ID       : 1
# Difficulty: Easy
# Tags     : Array, Hash Table
# Runtime  : 1
# Memory   : 20528000
# Language : Python3
# Solved   : 2026-06-06 17:38
# URL      : https://leetcode.com/problems/two-sum/
############################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i,dic[target - nums[i]]]
            else:
                dic.update({nums[i]:i})
        return [-1,-1]
        