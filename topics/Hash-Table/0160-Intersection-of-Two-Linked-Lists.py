############################################################
# Problem  : Intersection of Two Linked Lists
# ID       : 160
# Difficulty: Easy
# Tags     : Hash Table, Linked List, Two Pointers
# Runtime  : 112
# Memory   : 37996000
# Language : Python3
# Solved   : 2026-09-11 21:48
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
        cnt = 0

        while True:

            if p1 == p2:
                return p1
            
            p1 = p1.next
            p2 = p2.next

            if p1 == None:
                p1 = headB
                cnt += 1
            if p2 == None:
                p2 = headA
            
            if cnt > 1:
                return None
