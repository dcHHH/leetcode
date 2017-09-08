'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == len(nums):
            return sum(nums) / k
        i = 0
        ans, kSum = sum(nums[i: i + k]), sum(nums[i: i + k])
        for i in range(1, len(nums) - k + 1):
            kSum = kSum + nums[i+k-1] - nums[i-1]
            ans = max(ans, kSum)
        return ans / k

class Solution:
    def findMaxAverage(self, nums, k):
    	sums = [0] + list(itertools.accumulate(nums))
    	return max(map(operator.sub, sums[k:], sums[])) / k