'''


844. Backspace String Compare


Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

'''

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        stack1 = []
        for i in S:
            if i == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
                
        stack2 = []
        for i in T:
            if i == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        
        if len(stack1) != len(stack2):
            return False
        
        for i, j in zip(stack1, stack2):
            if i != j:
                return False

        return True

