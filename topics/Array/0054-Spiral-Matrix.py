############################################################
# Problem  : Spiral Matrix
# ID       : 54
# Difficulty: Medium
# Tags     : Array, Matrix, Simulation
# Runtime  : 0
# Memory   : 19404000
# Language : Python3
# Solved   : 2026-05-23 22:38
# URL      : https://leetcode.com/problems/spiral-matrix/
############################################################
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rs = 0
        re = len(matrix)-1
        cs = 0
        ce = len(matrix[0])-1
        while rs<=re and cs <= ce:
            for i in range(cs,ce+1):
                ans.append(matrix[rs][i])
            rs += 1
            for i in range(rs,re+1):
                ans.append(matrix[i][ce])
            ce -= 1
            if rs <= re:
                for i in range(ce,cs-1,-1):
                    ans.append(matrix[re][i])
                re -= 1
            if cs <= ce:
                for i in range(re,rs-1,-1):
                    ans.append(matrix[i][cs])
                cs += 1
        return ans

        