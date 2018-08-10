"""


15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        N, result = len(nums), []
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = nums[i] * -1
            start, end = i + 1, N - 1

            while start < end:
                
                if nums[start] + nums[end] != target:
                    if nums[start] + nums[end] < target:
                        start += 1
                    else:
                        end -= 1
                    continue
                elif start != i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue

                result.append((-1 * target, nums[start], nums[end]))
                start += 1
        
        return result
