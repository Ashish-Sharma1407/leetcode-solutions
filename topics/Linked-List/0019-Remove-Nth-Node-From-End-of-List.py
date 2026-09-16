############################################################
# Problem  : Remove Nth Node From End of List
# ID       : 19
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Runtime  : 0
# Memory   : 19292000
# Language : Python3
# Solved   : 2026-09-11 20:00
# URL      : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp != None:
            temp = temp.next
            cnt += 1
        
        temp = head
        place = cnt - n
        if place == 0:
            return head.next
        for i in range(1,place):
            temp = temp.next
        
        temp.next = temp.next.next
        return head
