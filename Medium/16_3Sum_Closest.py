'''


16. 3Sum Closest


Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        result = 999999999
        nums.sort()
        
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    temp = nums[i] + nums[l] + nums[r]
                    if abs(temp - target) < abs(result - target):
                        result = temp
                    
                    if temp < target:
                        l += 1
                    elif temp > target:
                        r -= 1
                    else:
                        return target
        return result

