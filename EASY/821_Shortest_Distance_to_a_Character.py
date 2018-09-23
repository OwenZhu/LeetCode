'''


821. Shortest Distance to a Character


Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        result = [None] * len(S)
        
        count = None
        for i, v in enumerate(S):
            if v == C:
                count = 0
            
            if not count is None:
                result[i] = count
                count += 1
        
        count = None
        for i, v in enumerate(reversed(S)):

            if v == C:
                count = 0
            
            if not count is None:
                if result[len(S) - 1 - i] is None:
                    result[len(S) - 1 - i] = count
                else:
                    result[len(S) - 1 - i] = min(count, result[len(S) - 1 - i])

                count += 1
        
        return result


