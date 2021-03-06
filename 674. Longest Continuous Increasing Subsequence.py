'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''

#o(n)time,o(n)space
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = [1] * len(nums)
        ind = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ans[ind] += 1
            else:
                ind = i
        return max(ans)

#o(n)time,o(1)space
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, 0
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                right += 1
                ans = max(ans, right - left + 1)
            else:
                left, right = i, i
        return ans