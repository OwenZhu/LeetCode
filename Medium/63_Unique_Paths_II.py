'''


63. Unique Paths II


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.


Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        maze = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        
        if not obstacleGrid[0][0]:
            maze[0][0] = 1

        i = 0
        while i < len(obstacleGrid):
            j = 0
            while j < len(obstacleGrid[0]):
                
                if not obstacleGrid[i][j]:
                    if i - 1 >= 0:
                        maze[i][j] += maze[i - 1][j]
                    if j - 1 >= 0:
                        maze[i][j] += maze[i][j - 1]

                j += 1
            
            i += 1
                    
        return maze[-1][-1]
