############################################################
# Problem  : Next Greater Element I
# ID       : 496
# Difficulty: Easy
# Tags     : Array, Hash Table, Stack, Monotonic Stack
# Runtime  : 0
# Memory   : 19304000
# Language : Python3
# Solved   : 2026-07-05 10:57
# URL      : https://leetcode.com/problems/next-greater-element-i/
############################################################
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        st = []
        result = []
        for i in range(len(nums2)-1,-1,-1):
            while len(st) > 0 and st[-1] <= nums2[i]:
                st.pop()
            if len(st)==0:
                ans.update({nums2[i]: -1})
            else:
                ans.update({nums2[i]: st[-1]})
            st.append(nums2[i])
        for num in nums1:
            result.append(ans[num])
        return result


        