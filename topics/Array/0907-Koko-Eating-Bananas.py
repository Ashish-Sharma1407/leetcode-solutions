############################################################
# Problem  : Koko Eating Bananas
# ID       : 907
# Difficulty: Medium
# Tags     : Array, Binary Search
# Runtime  : 155
# Memory   : 20576000
# Language : Python3
# Solved   : 2026-06-30 10:17
# URL      : https://leetcode.com/problems/koko-eating-bananas/
############################################################
class Solution:
    def eatHours(self,piles,mid):
        ans = 0
        for pile in piles:
            ans += (pile + mid - 1) // mid
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            mid = (l + r)// 2
            eat_hour = self.eatHours(piles,mid)

            if eat_hour > h:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans
