'''


884. Uncommon Words from Two Sentences


We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

'''

from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = Counter(A.split(" "))
        B = Counter(B.split(" "))
        
        res = []
        for i in A.keys():
            if not i in B and A[i] == 1:
                res.append(i)
                
        for i in B:
            if not i in A and B[i] == 1:
                res.append(i)
        
        return res


