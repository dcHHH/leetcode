'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while head is not slow:
                    head, slow = head.next, slow.next
                return head
        return None