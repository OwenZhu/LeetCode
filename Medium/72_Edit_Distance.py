'''


72. Edit Distance


Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        ed_mat = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        
        
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0:
                    ed_mat[i][j] = j  
                elif j == 0:
                    ed_mat[i][j] = i
                else:
                    
                    if word1[j - 1] != word2[i - 1]:
                        ed_mat[i][j] = 1
                    
                    ed_mat[i][j] = min(ed_mat[i - 1][j] + 1, ed_mat[i][j - 1] + 1, ed_mat[i][j] + ed_mat[i - 1][j - 1])

        return ed_mat[-1][-1]
