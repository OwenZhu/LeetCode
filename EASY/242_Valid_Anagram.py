'''


242. Valid Anagram


Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''

from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        
        for i in t:
            s_dict[i] -= 1
            if s_dict[i] < 0:
                return False
            
        if sum(s_dict.values()):
            return False
        else:
            return True
