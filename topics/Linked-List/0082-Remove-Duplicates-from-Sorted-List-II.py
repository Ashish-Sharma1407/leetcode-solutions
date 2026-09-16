############################################################
# Problem  : Remove Duplicates from Sorted List II
# ID       : 82
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Runtime  : 0
# Memory   : 19276000
# Language : Python3
# Solved   : 2026-09-11 21:00
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
############################################################
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  # skip the entire duplicate run
            else:
                prev = curr            # no duplicate — advance prev normally
            curr = curr.next

        return dummy.next