############################################################
# Problem  : Majority Element
# ID       : 169
# Difficulty: Easy
# Tags     : Array, Hash Table, Divide and Conquer, Sorting, Counting
# Runtime  : 8
# Memory   : 21072000
# Language : Python3
# Solved   : 2026-07-19 18:29
# URL      : https://leetcode.com/problems/majority-element/
############################################################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        ans = 0
        for i in range(len(nums)):
            if freq == 0:
                ans = nums[i]
                freq = 1
            elif nums[i] == ans:
                freq += 1
            else: 
                freq -= 1
        return ans
        