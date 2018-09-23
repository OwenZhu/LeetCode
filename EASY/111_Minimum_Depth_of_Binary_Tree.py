'''


111. Minimum Depth of Binary Tree


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node.left and not node.right:
                return 1
            
            min_depth = 999999
            if node.left:
                l = dfs(node.left) + 1
                min_depth = min(min_depth, l)
            if node.right:
                r = dfs(node.right) + 1
                min_depth = min(min_depth, r)
                
            return min_depth
        
        if not root:
            return 0
        return dfs(root)


