'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, l = 1, len(nums)
        ans = []
        for i in range(l):
            ans.append(a)
            a *= nums[i]
        a = 1
        for i in reversed(range(l)):
            ans[i] *= a
            a *= nums[i]
        return ans