'''


907. Sum of Subarray Minimums


Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000

'''

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n, mod = len(A), 10**9 + 7
        left, right = [0] * n, [0] * n
        
        stack1 = []
        for i in range(n):
            count = 1
            
            while stack1 and stack1[-1][0] > A[i]:
                count += stack1.pop()[1]
                
            left[i] = count
            stack1.append((A[i], count))
            
        stack2 = []
        for i in range(n)[::-1]:
            count = 1
            
            while stack2 and stack2[-1][0] >= A[i]:
                count += stack2.pop()[1]
                
            right[i] = count
            stack2.append((A[i], count))
        
        
        return sum([a * l * r for a, l, r in zip(A, left, right)]) % mod


