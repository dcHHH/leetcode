'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

#O(n) space and O(n) time
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums
        for x in s:
            if s[abs(x) - 1] < 0:
                return abs(x)
            else:
                s[abs(x) - 1] *= -1
        return False

#O(1) space and O(nlogn) time
class Solution(object):
    def findDuplicate(self, nums):
        left, right = 1, len(nums)-1
        while left < right:
           mid = (right + left) // 2
           left, right = [left, mid] if sum(i <= mid for i in nums) > mid else [mid+1, right]
        return right

#O(1) space and O(n) time
class Solution(Thread):
	def findDuplicate(self, nums):
	    slow = fast = finder = 0
	    while True:
	        slow = nums[slow]
	        fast = nums[nums[fast]]
	        if slow == fast:
	            while finder != slow:
	                finder = nums[finder]
	                slow = nums[slow]
	            return finder