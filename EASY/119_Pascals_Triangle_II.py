'''


119. Pascal's Triangle II


Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result = []
        for i in range(rowIndex + 1):
            result.append([1 for _ in range(i + 1)])

        for i in range(rowIndex):
            if i > 0:
                for j in range(len(result[i]) - 1):
                    result[i + 1][j + 1] = result[i][j] + result[i][j + 1]

        return result[-1]

