############################################################
# Problem  : Binary Tree Postorder Traversal
# ID       : 145
# Difficulty: Easy
# Tags     : Stack, Tree, Depth-First Search, Binary Tree
# Runtime  : 0
# Memory   : 19472000
# Language : Python3
# Solved   : 2026-07-09 07:44
# URL      : https://leetcode.com/problems/binary-tree-postorder-traversal/
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
    
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder(root)
        return self.ans
        