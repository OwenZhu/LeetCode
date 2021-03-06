'''


142. Linked List Cycle II


Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

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
        fast = head
        slow = head
        meet = None
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast is slow:
                meet = fast
                break
        
        if not meet:
            return
        
        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next

