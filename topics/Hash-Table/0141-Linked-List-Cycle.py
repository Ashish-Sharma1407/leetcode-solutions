############################################################
# Problem  : Linked List Cycle
# ID       : 141
# Difficulty: Easy
# Tags     : Hash Table, Linked List, Two Pointers
# Runtime  : 59
# Memory   : 22552000
# Language : Python3
# Solved   : 2026-07-01 20:24
# URL      : https://leetcode.com/problems/linked-list-cycle/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        else:
            return False
        