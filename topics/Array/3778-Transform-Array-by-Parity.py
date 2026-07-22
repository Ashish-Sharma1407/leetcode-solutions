############################################################
# Problem  : Transform Array by Parity
# ID       : 3778
# Difficulty: Easy
# Tags     : Array, Sorting, Counting
# Runtime  : 1
# Memory   : 19312000
# Language : Python3
# Solved   : 2026-07-22 21:24
# URL      : https://leetcode.com/problems/transform-array-by-parity/
############################################################
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans =[]
        for num in nums:
            if num % 2 == 0:
                ans.append(0)
            elif num % 2 != 0:
                ans.append(1)
        ans.sort()
        return ans
        