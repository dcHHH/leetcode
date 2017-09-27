‘’‘
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
‘’‘

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for k in range(len(nums)):
            val = nums[k]
            nums[k] = 2
            if val < 2:
                nums[j] = 1
                j += 1
            if val == 0:
                nums[i] = 0
                i += 1