############################################################
# Problem  : Rotate List
# ID       : 61
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Runtime  : 0
# Memory   : 19412000
# Language : Python3
# Solved   : 2026-07-01 13:21
# URL      : https://leetcode.com/problems/rotate-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        if head == None or head.next == None:
            return head

        cnt = 0
        curr = head
        while curr != None:
            cnt += 1
            curr = curr.next  
        k = k % cnt

        if k == 0:
            return head

        for i in range(k):
            p2 = p2.next
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        temp = p1.next
        p1.next = None
        p2.next = head
        return temp

        