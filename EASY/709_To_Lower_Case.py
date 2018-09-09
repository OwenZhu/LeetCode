'''


709. To Lower Case


Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase. 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

'''

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        result = []
        for char in str:
            ascii_value = ord(char)
            if ascii_value >= 65 and ascii_value <= 90:
                ascii_value += 32
            
            result += chr(ascii_value)
        
        return "".join(result)

