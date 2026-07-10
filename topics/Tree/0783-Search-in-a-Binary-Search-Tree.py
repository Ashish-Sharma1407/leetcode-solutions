############################################################
# Problem  : Search in a Binary Search Tree
# ID       : 783
# Difficulty: Easy
# Tags     : Tree, Binary Search Tree, Binary Tree
# Runtime  : 0
# Memory   : 20964000
# Language : Python3
# Solved   : 2026-07-10 13:26
# URL      : https://leetcode.com/problems/search-in-a-binary-search-tree/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None

        curr = root

        while curr != None:
            if target == curr.val:
                return curr
            elif target > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr
        