############################################################
# Problem  : Remove Nth Node From End of List
# ID       : 19
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Runtime  : 0
# Memory   : 19304000
# Language : Python3
# Solved   : 2026-07-01 10:39
# URL      : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        for i in range(n):
            p2 = p2.next

        if p2 == None:
            head = p1.next
            return head

        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next
        return head
        