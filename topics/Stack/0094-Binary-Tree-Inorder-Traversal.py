############################################################
# Problem  : Binary Tree Inorder Traversal
# ID       : 94
# Difficulty: Easy
# Tags     : Stack, Tree, Depth-First Search, Binary Tree
# Runtime  : 0
# Memory   : 19384000
# Language : Python3
# Solved   : 2026-07-09 08:05
# URL      : https://leetcode.com/problems/binary-tree-inorder-traversal/
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
    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.ans
        