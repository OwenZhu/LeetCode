'''


75. Sort Colors


Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def merge_sort(lst):
            if len(lst) <= 1:
                return
            
            left = lst[:len(lst) // 2]
            right = lst[len(lst) // 2:]
            
            merge_sort(left)
            merge_sort(right)
            
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                
                k += 1
                
            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1
        
        merge_sort(nums)
