############################################################
# Problem  : Delete Node in a BST
# ID       : 450
# Difficulty: Medium
# Tags     : Tree, Binary Search Tree, Binary Tree
# Runtime  : 0
# Memory   : 22172000
# Language : Python3
# Solved   : 2026-07-11 10:53
# URL      : https://leetcode.com/problems/delete-node-in-a-bst/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None

        elif key > root.val:
            root.right = self.deleteNode(root.right,key)

        elif key < root.val:
            root.left = self.deleteNode(root.left,key)

        else:
            if root.right is None and root.left is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                temp = root.right
                while temp.left != None:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        
        return root

        