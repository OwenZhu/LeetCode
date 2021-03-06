'''


507. Perfect Number


We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

'''

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 1:
            return False
        
        divisors_sum = 0
        for i in range(2, num):
            n, m = divmod(num, i)
            if i > n:
                break
                
            if not m:
                divisors_sum += (n + i)

        return (divisors_sum + 1) == num

