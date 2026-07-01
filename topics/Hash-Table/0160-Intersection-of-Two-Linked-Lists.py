############################################################
# Problem  : Intersection of Two Linked Lists
# ID       : 160
# Difficulty: Easy
# Tags     : Hash Table, Linked List, Two Pointers
# Runtime  : 109
# Memory   : 38264000
# Language : Python3
# Solved   : 2026-07-01 17:26
# URL      : https://leetcode.com/problems/intersection-of-two-linked-lists/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        return p1

            
        