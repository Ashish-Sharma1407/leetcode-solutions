############################################################
# Problem  : Last Stone Weight
# ID       : 1127
# Difficulty: Easy
# Tags     : Array, Heap (Priority Queue)
# Runtime  : 0
# Memory   : 19316000
# Language : Python3
# Solved   : 2026-07-12 09:04
# URL      : https://leetcode.com/problems/last-stone-weight/
############################################################
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for num in stones:
            heapq.heappush(h,-num)
        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            if abs(a-b) != 0:
                heapq.heappush(h,-abs(a-b))
        if len(h) != 0:
            return -heapq.heappop(h)
        return 0

            
        