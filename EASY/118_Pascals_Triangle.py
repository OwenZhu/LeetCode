'''


118. Pascal's Triangle


Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = []
        for i in range(numRows):
            result.append([1 for _ in range(i + 1)])
            
        for i in range(numRows - 1):
            if i > 0:
                for j in range(len(result[i]) - 1):
                    result[i + 1][j + 1] = result[i][j] + result[i][j + 1]
                    
        return result


