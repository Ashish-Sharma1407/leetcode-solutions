############################################################
# Problem  : Majority Element
# ID       : 169
# Difficulty: Easy
# Tags     : Array, Hash Table, Divide and Conquer, Sorting, Counting
# Runtime  : 5
# Memory   : 21128000
# Language : Python3
# Solved   : 2026-05-31 16:51
# URL      : https://leetcode.com/problems/majority-element/
############################################################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        ans = 0
        for val in nums:
            if freq == 0:
                ans = val
                freq = 1
            elif ans == val:
                freq += 1
            else:
                freq -= 1
        return ans
        