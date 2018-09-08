'''


589. N-ary Tree Preorder Traversal


Given an n-ary tree, return the preorder traversal of its nodes' values.
 
For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        def dfs(node, result):
            if not node:
                return
            
            result.append(node.val)

            for c in node.children:
                dfs(c, result)
        
        result = []
        dfs(root, result)
        return result
