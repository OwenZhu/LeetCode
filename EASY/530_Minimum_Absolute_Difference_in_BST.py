'''


530. Minimum Absolute Difference in BST


Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = float('inf')
        self.prev = -float('inf')
        
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            self.res = min(abs(node.val - self.prev), self.res)
            self.prev = node.val
            dfs(node.right)
        
        dfs(root)
        return self.res

