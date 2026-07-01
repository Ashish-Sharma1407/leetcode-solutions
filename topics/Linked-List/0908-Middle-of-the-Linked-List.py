############################################################
# Problem  : Middle of the Linked List
# ID       : 908
# Difficulty: Easy
# Tags     : Linked List, Two Pointers
# Runtime  : 0
# Memory   : 19372000
# Language : Python3
# Solved   : 2026-07-01 09:30
# URL      : https://leetcode.com/problems/middle-of-the-linked-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        