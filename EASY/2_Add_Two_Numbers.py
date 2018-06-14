"""


2. Add Two Numbers


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_list = curr_node = ListNode(0)
        
        carry_bit = False
        
        while l1 or l2 or carry_bit:

            curr_val = 0
            
            if l1:
                curr_val += l1.val
                l1 = l1.next
                if l2:
                    curr_val += l2.val
                    l2 = l2.next
            elif l2:
                curr_val += l2.val
                l2 = l2.next
            
            if carry_bit:
                curr_val += 1
                carry_bit = False
            
            if curr_val >= 10:
                curr_val = curr_val % 10
                carry_bit = True
            
            curr_node.next = ListNode(curr_val)
            curr_node = curr_node.next
        
        return r_list.next