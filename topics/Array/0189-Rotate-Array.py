############################################################
# Problem  : Rotate Array
# ID       : 189
# Difficulty: Medium
# Tags     : Array, Math, Two Pointers
# Runtime  : 6
# Memory   : 26496000
# Language : Python3
# Solved   : 2026-06-04 10:01
# URL      : https://leetcode.com/problems/rotate-array/
############################################################
class Solution:
    def rev(self,nums,left,right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.rev(nums,n-k,n-1)
        self.rev(nums,0,n-k-1)
        self.rev(nums,0,n-1)
