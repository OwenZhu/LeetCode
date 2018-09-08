'''


590. N-ary Tree Postorder Traversal


Given an n-ary tree, return the postorder traversal of its nodes' values.

 
For example, given a 3-ary tree:


Return its postorder traversal as: [5,6,3,2,4,1].


'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(node, result):
            if not node:
                return

            for c in node.children:
                dfs(c, result)
                
            result.append(node.val)
        
        result = []
        dfs(root, result)
        return result
