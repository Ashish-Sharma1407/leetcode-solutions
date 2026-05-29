############################################################
# Problem  : Shuffle the Array
# ID       : 1580
# Difficulty: Easy
# Tags     : Array
# Runtime  : 58
# Memory   : 19440000
# Language : Python3
# Solved   : 2026-05-29 19:13
# URL      : https://leetcode.com/problems/shuffle-the-array/
############################################################
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        ans = []
        i = 0
        j = n
        while j < len(nums):
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans


        