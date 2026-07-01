############################################################
# Problem  : Linked List Cycle II
# ID       : 142
# Difficulty: Medium
# Tags     : Hash Table, Linked List, Two Pointers
# Runtime  : 50
# Memory   : 22404000
# Language : Python3
# Solved   : 2026-07-01 21:17
# URL      : https://leetcode.com/problems/linked-list-cycle-ii/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        hascycle = False

        while fast != None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hascycle = True
                break
        
        if hascycle == False:
            return None

        slow = slow.next
        cyclenodes = 1
        while slow != fast:
            slow = slow.next
            cyclenodes += 1
        
        slow = head
        fast = head

        for i in range(cyclenodes):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
            
        
        

