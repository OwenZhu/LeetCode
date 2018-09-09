'''


113. Path Sum II


Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        def dfs(node, curr_path, lst, target):
            
            if not node:
                return

            curr_path.append(node.val)
            
            if not node.left and not node.right and sum(curr_path) == target:
                lst.append(curr_path)
                return

            if node.left:
                dfs(node.left, list(curr_path), lst, target)
            if node.right:
                dfs(node.right, list(curr_path), lst, target)
        
        result = []
        dfs(root, [], result, sum_)
        return result
