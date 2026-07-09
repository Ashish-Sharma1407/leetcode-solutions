############################################################
# Problem  : Binary Tree Right Side View
# ID       : 199
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Runtime  : 4
# Memory   : 19336000
# Language : Python3
# Solved   : 2026-07-09 20:15
# URL      : https://leetcode.com/problems/binary-tree-right-side-view/
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:

    def __init__(self):
        self.arr = []
        self.length = 0
        self.front = 0

    def push(self, item):
        self.arr.append(item)
        self.length += 1

    
    def pop(self):
        if len(self.arr) == 0:
            return None
        x = self.arr[self.front]
        self.length -= 1
        self.front += 1
        return x

    def front(self):
        if len(self.arr) == 0:
            return None
        return self.arr[self.front]

    def size(self):
        return self.length

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = Queue()
        ans = []

        if root is None:
            return ans

        queue.push(root)
        ans.append(root.val)

        while queue.size() > 0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                
                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)

                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)
            
            if len(level) > 0:
                ans.append(level[-1])
    
        return ans