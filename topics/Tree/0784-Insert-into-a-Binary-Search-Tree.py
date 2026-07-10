############################################################
# Problem  : Insert into a Binary Search Tree
# ID       : 784
# Difficulty: Medium
# Tags     : Tree, Binary Search Tree, Binary Tree
# Runtime  : 0
# Memory   : 21232000
# Language : Python3
# Solved   : 2026-07-10 13:51
# URL      : https://leetcode.com/problems/insert-into-a-binary-search-tree/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newnode = TreeNode(val)
        if root is None:
            return newnode

        curr = root

        while curr != None:

            if curr.val > newnode.val:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = newnode
                    break

            else:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = newnode
                    break
        
        return root
