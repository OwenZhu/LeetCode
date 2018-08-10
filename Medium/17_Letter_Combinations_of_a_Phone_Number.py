'''


17. Letter Combinations of a Phone Number


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution:
    def combination(self, list1, list2):
        comb = []
        for i in list1:
            for j in list2:
                comb.append(i + j)
        return sorted(comb)
    
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key_dict = {'2': 'abc', '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        
        for d in digits:
            print(key_dict[d], result)
            result = self.combination(result, key_dict[d])
            
        if result == [""]:
            return []
        
        return result