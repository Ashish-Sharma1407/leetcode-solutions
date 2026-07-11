############################################################
# Problem  : Validate Binary Search Tree
# ID       : 98
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Runtime  : 3
# Memory   : 20852000
# Language : Python3
# Solved   : 2026-07-11 11:56
# URL      : https://leetcode.com/problems/validate-binary-search-tree/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, mn, mx):
        if root is None:
            return True
        
        elif root.val< mn or root.val > mx:
            return False

        checkleft = self.check(root.left, mn, root.val - 1)
        checkright = self.check(root.right, root.val+1, mx)

        return checkleft and checkright


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,-1000000000000000,10000000000000)

        