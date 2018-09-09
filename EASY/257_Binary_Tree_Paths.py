'''


257. Binary Tree Paths


Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def dfs(node, curr_path, lst):
            
            if not node:
                return
            
            curr_path += "->" + str(node.val)
            
            if not node.left and not node.right:
                lst.append(curr_path[2:])
                return

            if node.left:
                dfs(node.left, curr_path, lst)
            if node.right:
                dfs(node.right, curr_path, lst)
        
        result = []
        dfs(root, "", result)
        return result
