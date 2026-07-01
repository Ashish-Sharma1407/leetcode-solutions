############################################################
# Problem  : Delete Node in a Linked List
# ID       : 237
# Difficulty: Medium
# Tags     : Linked List
# Runtime  : 43
# Memory   : 19484000
# Language : Python3
# Solved   : 2026-07-01 09:45
# URL      : https://leetcode.com/problems/delete-node-in-a-linked-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next
        