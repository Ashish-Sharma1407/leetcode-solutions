############################################################
# Problem  : Add Two Numbers
# ID       : 2
# Difficulty: Medium
# Tags     : Linked List, Math, Recursion
# Runtime  : 8
# Memory   : 19200000
# Language : Python3
# Solved   : 2026-07-14 12:02
# URL      : https://leetcode.com/problems/add-two-numbers/
############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2

        ans = ListNode(-1)
        curr3 = ans
        carry = 0

        while curr1 != None or curr2 != None:
            total = 0
            total += carry
            carry = 0

            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next

            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next

            if total > 9:
                carry = 1
                total -= 10

            newNode = ListNode(total)
            curr3.next = newNode
            curr3 = curr3.next

        if carry > 0:
            newNode = ListNode(carry)
            curr3.next = newNode
            curr3 = curr3.next

        return ans.next
