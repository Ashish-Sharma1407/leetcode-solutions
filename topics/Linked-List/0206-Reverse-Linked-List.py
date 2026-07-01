############################################################
# Problem  : Reverse Linked List
# ID       : 206
# Difficulty: Easy
# Tags     : Linked List, Recursion
# Runtime  : 0
# Memory   : 20432000
# Language : Python3
# Solved   : 2026-07-01 11:41
# URL      : https://leetcode.com/problems/reverse-linked-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev




        