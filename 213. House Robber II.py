'''
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(nums):
            pre, cur = 0, 0
            for i in nums:
                pre, cur = cur , max(cur, pre + i)
            return cur
        return max(rob(nums[1:]), rob(nums[:-1])) if len(nums) != 1 else nums[0]