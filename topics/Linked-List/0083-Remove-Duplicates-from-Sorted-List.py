############################################################
# Problem  : Remove Duplicates from Sorted List
# ID       : 83
# Difficulty: Easy
# Tags     : Linked List
# Runtime  : 0
# Memory   : 19432000
# Language : Python3
# Solved   : 2026-09-11 20:15
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head

        dummy = ListNode(float('-inf'))
        temp = dummy

        curr = head
        while curr != None:
            if temp.val != curr.val:
                temp.next = ListNode(curr.val)
                temp = temp.next
            curr = curr.next
        return dummy.next

        