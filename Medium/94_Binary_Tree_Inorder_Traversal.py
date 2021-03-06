'''


94. Binary Tree Inorder Traversal


Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        stack = [root]
        curr_node = root
        result = []
        
        if not root:
            return result
        
        while stack:
            while curr_node and curr_node.left:
                stack.append(curr_node.left)
                curr_node = curr_node.left
            
            curr_node = stack.pop()
            
            if curr_node:
                result.append(curr_node.val)
                stack.append(curr_node.right)
                curr_node = curr_node.right
                
        return result
