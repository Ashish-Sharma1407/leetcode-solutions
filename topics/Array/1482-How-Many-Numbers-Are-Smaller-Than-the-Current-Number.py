############################################################
# Problem  : How Many Numbers Are Smaller Than the Current Number
# ID       : 1482
# Difficulty: Easy
# Tags     : Array, Hash Table, Sorting, Counting Sort
# Runtime  : 0
# Memory   : 19220000
# Language : Python3
# Solved   : 2026-05-29 20:11
# URL      : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
############################################################
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)

        dic = {}
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in dic:
                dic.update({sorted_arr[i]:i})
        ans = []
        for i in range(len(nums)):
            ans.append(dic[nums[i]])
        return ans

        