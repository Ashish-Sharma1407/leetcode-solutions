############################################################
# Problem  : Find Missing and Repeated Values
# ID       : 3227
# Difficulty: Easy
# Tags     : Array, Hash Table, Math, Matrix
# Runtime  : 24
# Memory   : 19668000
# Language : Python3
# Solved   : 2026-05-31 20:35
# URL      : https://leetcode.com/problems/find-missing-and-repeated-values/
############################################################
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dic = {}
        ans = []
        size = len(grid)

        for i in range(size*size):
            dic.update({i+1: 0})

        for i in range(size*size):
            row = i // size
            col = i % size
            if grid[row][col] in dic:
                dic[grid[row][col]] += 1
            else:
                dic.update({grid[row][col]:1})
        
        for key in dic.keys():
            if dic[key] > 1:
                ans.append(key)
        for key in dic.keys():
            if dic[key] == 0:
                ans.append(key)
        return ans
        
