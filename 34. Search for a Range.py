'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binsearch(left, right):
            if nums[left] == target == nums[right]:
                return [left, right]
            elif nums[left] <= target <= nums[right]:
                mid = (left + right) // 2
                l, r = binsearch(left, mid) , binsearch(mid + 1, right)
                return max(l, r) if -1 in l + r else [l[0], r[1]]
            return [-1, -1]
        return binsearch(0, len(nums) - 1) if nums else [-1,-1]