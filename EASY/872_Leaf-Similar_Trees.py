'''


872. Leaf-Similar Trees


Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(node, lst):
            if not node.left and not node.right:
                lst.append(node.val)
                return
            
            if node.left:
                dfs(node.left, lst)
                
            if node.right:
                dfs(node.right, lst)
        
        list_1 = []
        dfs(root1, list_1)
        
        list_2 = []
        dfs(root2, list_2)
        
        if len(list_1) != len(list_2):
            return False
        
        for i, j in zip(list_1, list_2):
            if i != j:
                return False
            
        return True


