############################################################
# Problem  : Merge Two Sorted Lists
# ID       : 21
# Difficulty: Easy
# Tags     : Linked List, Recursion
# Runtime  : 0
# Memory   : 19268000
# Language : Python3
# Solved   : 2026-11-17 19:20
# URL      : https://leetcode.com/problems/merge-two-sorted-lists/
############################################################
class Solution:
    def mergeTwoLists(self, list1, list2):
        d = ListNode()
        current = d
        while list1 or list2:
            v1 = list1.val if list1 else float('inf')
            v2 = list2.val if list2 else float('inf')

            if v1 < v2:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        return d.next