############################################################
# Problem  : Search a 2D Matrix
# ID       : 74
# Difficulty: Medium
# Tags     : Array, Binary Search, Matrix
# Runtime  : 0
# Memory   : 19688000
# Language : Python3
# Solved   : 2026-06-30 10:29
# URL      : https://leetcode.com/problems/search-a-2d-matrix/
############################################################
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid = (l + r) // 2
            if (matrix[mid//cols][mid%cols] == target):
                return True
            elif matrix[mid//cols][mid%cols] < target:
                l = mid + 1
            else:
                r = mid - 1
        return  False
