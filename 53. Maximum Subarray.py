'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndHere, ans = nums[0], nums[0]
        for i in nums[1:]:
            maxEndHere = max(i, i + maxEndHere)
            ans = max(ans, maxEndHere)
        return ans