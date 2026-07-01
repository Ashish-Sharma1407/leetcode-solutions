############################################################
# Problem  : Remove Duplicates from Sorted List
# ID       : 83
# Difficulty: Easy
# Tags     : Linked List
# Runtime  : 0
# Memory   : 19216000
# Language : Python3
# Solved   : 2026-07-01 11:18
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        while curr.next != None and curr != None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
        