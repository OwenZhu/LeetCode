'''


64. Minimum Path Sum


Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        value_mat = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        i = 0
        while i < len(grid):
            
            j = 0
            while j < len(grid[0]):
                
                if i == j == 0:
                    pre_value = 0
                else:
                    pre_value = float('Inf')
                    if i - 1 >= 0:
                        pre_value = min(pre_value, value_mat[i - 1][j])
                    if j - 1 >= 0:
                        pre_value = min(pre_value, value_mat[i][j - 1])
                    
                value_mat[i][j] = pre_value + grid[i][j]
                j += 1
            
            i += 1
        
        return value_mat[-1][-1]
