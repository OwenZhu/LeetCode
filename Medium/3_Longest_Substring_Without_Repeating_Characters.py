"""


3. Longest Substring Without Repeating Characters


Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        used_set = dict()
        max_length = 0

        # sliding window
        i = j = 0
        while i < len(s) and j < len(s):
            if not s[j] in used_set or used_set[s[j]] < i:
                used_set[s[j]] = j
                max_length = max(max_length, j - i + 1)
                j += 1
            else:
                i = used_set[s[j]] + 1
                
        return max_length