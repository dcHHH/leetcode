'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
#o(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        ans = [1] * l
        for i in range(1, l):
            for j in range(i):
                if nums[j] < nums[i]:
                    ans[i] = max(ans[i], ans[j] + 1)
        return max(ans)

#o(nlogn)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binsearch(num, left, right, target):
            if left == right:
                return left
            mid = (left + right) / 2
            return binsearch(num, mid + 1, right, target) if num[mid] < target else binsearch(num, left, mid, target)
        ans = []
        for num in nums:
            pos = binsearch(ans, 0, len(ans), num)
            if pos >= len(ans):
                ans.append(num)
            else:
                ans[pos] = num
        return len(ans)