############################################################
# Problem  : Concatenation of Array
# ID       : 2058
# Difficulty: Easy
# Tags     : Array, Simulation
# Runtime  : 0
# Memory   : 19276000
# Language : Python3
# Solved   : 2026-05-23 22:41
# URL      : https://leetcode.com/problems/concatenation-of-array/
############################################################
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
        