############################################################
# Problem  : Rotate List
# ID       : 61
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Runtime  : 0
# Memory   : 19388000
# Language : Python3
# Solved   : 2026-09-11 21:16
# URL      : https://leetcode.com/problems/rotate-list/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None:
            return head
            
        curr = head
        cnt = 0
        while curr.next != None:
            curr = curr.next
            cnt += 1
        cnt += 1
        
        k = k % cnt
        if k == 0:
            return head
        place = cnt - k

        temp = head
        for i in range(1,place):
            temp = temp.next
        
        curr.next = head
        head = temp.next
        temp.next = None
    
        return head

