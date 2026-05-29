############################################################
# Problem  : Set Mismatch
# ID       : 645
# Difficulty: Easy
# Tags     : Array, Hash Table, Bit Manipulation, Sorting
# Runtime  : 8
# Memory   : 21232000
# Language : Python3
# Solved   : 2026-05-29 19:51
# URL      : https://leetcode.com/problems/set-mismatch/
############################################################
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeat = 0
        act_sum = (len(nums)*(len(nums)+1))//2
        curr_sum = 0
        s = set()
        for val in nums:
            if val in s:
                repeat = val
            else:
                s.add(val)
                curr_sum += val
        return [repeat, act_sum - curr_sum]
        
        
        

        