############################################################
# Problem  : Running Sum of 1d Array
# ID       : 1603
# Difficulty: Easy
# Tags     : Array, Prefix Sum
# Runtime  : 0
# Memory   : 19356000
# Language : Python3
# Solved   : 2026-06-19 08:49
# URL      : https://leetcode.com/problems/running-sum-of-1d-array/
############################################################
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 0:
            return nums
        ans = []
        add = 0
        for i in range(len(nums)):
            add = add + nums[i]
            ans.append(add)
        return ans

        