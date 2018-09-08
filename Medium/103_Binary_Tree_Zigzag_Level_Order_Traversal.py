'''


103. Binary Tree Zigzag Level Order Traversal


Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = 0
        result = []
        bfs = [(level, root)]

        curr = []
        
        while len(bfs):
            l, node = bfs.pop(0)
            
            if level != l:
                if not level % 2:
                    result.append(curr)
                else:
                    result.append(curr[::-1])
                    
                curr = []
                level = l
            
            if node:
                bfs.append((l + 1, node.left))
                bfs.append((l + 1, node.right))
                curr.append(node.val)

        return result

