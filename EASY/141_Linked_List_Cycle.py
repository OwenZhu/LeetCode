'''


141. Linked List Cycle


Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = head
        slow = head
        
        count = 0
        while fast and slow:
            fast = fast.next
            if count % 2:
                slow = slow.next
                
            if fast is slow:
                return True
                
            count += 1
            
        return False

