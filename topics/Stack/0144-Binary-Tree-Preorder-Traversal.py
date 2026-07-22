############################################################
# Problem  : Binary Tree Preorder Traversal
# ID       : 144
# Difficulty: Easy
# Tags     : Stack, Tree, Depth-First Search, Binary Tree
# Runtime  : 0
# Memory   : 19288000
# Language : Python3
# Solved   : 2026-07-22 11:06
# URL      : https://leetcode.com/problems/binary-tree-preorder-traversal/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self,root):
        if root is None:
            return
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.ans
        