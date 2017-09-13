'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = node
            node = cur
        while head and node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True