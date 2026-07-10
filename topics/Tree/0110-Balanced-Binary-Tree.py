############################################################
# Problem  : Balanced Binary Tree
# ID       : 110
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Tree
# Runtime  : 0
# Memory   : 20496000
# Language : Python3
# Solved   : 2026-07-10 11:12
# URL      : https://leetcode.com/problems/balanced-binary-tree/
############################################################
class Solution:
    def __init__(self):
        self.ans = True

    def height(self, root):
        if root is None:
            return 0

        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        if abs(leftheight - rightheight) > 1:
            self.ans = False

        return 1 + max(leftheight, rightheight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans