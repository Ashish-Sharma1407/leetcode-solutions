############################################################
# Problem  : Rotate Array
# ID       : 189
# Difficulty: Medium
# Tags     : Array, Math, Two Pointers
# Runtime  : 3
# Memory   : 26528000
# Language : Python3
# Solved   : 2026-07-25 20:20
# URL      : https://leetcode.com/problems/rotate-array/
############################################################
class Solution:
    def rev(self,left,right,nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.rev(n-k,n-1,nums)
        self.rev(0,n-k-1,nums)
        self.rev(0,n-1,nums)

        