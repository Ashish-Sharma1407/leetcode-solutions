############################################################
# Problem  : Maximum Depth of Binary Tree
# ID       : 104
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Runtime  : 7
# Memory   : 22396000
# Language : Python3
# Solved   : 2026-07-10 09:33
# URL      : https://leetcode.com/problems/maximum-depth-of-binary-tree/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) +1
        