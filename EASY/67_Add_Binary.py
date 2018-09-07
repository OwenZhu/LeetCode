"""


67. Add Binary


Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        c, i, j = 0, len(a) - 1, len(b) - 1
        result = ''
        
        while i >= 0 or j >= 0 or c:
            current_bit = c
            
            if i >= 0:
                current_bit += int(a[i])
                i -= 1
                
            if j >= 0:
                current_bit += int(b[j])
                j -= 1
                
            c = int(current_bit / 2)
            result = str(current_bit % 2) + result
        
        return result
