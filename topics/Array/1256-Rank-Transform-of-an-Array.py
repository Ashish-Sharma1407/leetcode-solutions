############################################################
# Problem  : Rank Transform of an Array
# ID       : 1256
# Difficulty: Easy
# Tags     : Array, Hash Table, Sorting
# Runtime  : 64
# Memory   : 37568000
# Language : Python3
# Solved   : 2026-11-18 20:13
# URL      : https://leetcode.com/problems/rank-transform-of-an-array/
############################################################
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        
        if len(arr) == 0:
            return arr

        temp = sorted(arr)
        dic = {}
        ans = []
        count = 1

        for i in range(len(temp)):
            if temp[i] in dic:
                continue
            else:
                dic.update({temp[i]: count})
                count += 1
        
        for num in arr:
            ans.append(dic[num])

        return ans

        

        
        
        
        