############################################################
# Problem  : Running Sum of 1d Array
# ID       : 1603
# Difficulty: Easy
# Tags     : Array, Prefix Sum
# Runtime  : 0
# Memory   : 19444000
# Language : Python3
# Solved   : 2026-09-10 19:26
# URL      : https://leetcode.com/problems/running-sum-of-1d-array/
############################################################
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        ele = 0
        for num in nums:
            ele += num
            ans.append(ele)
        return ans
        