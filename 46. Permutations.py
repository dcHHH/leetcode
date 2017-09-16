'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]


    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]


	def permute(self, nums):
	    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
	                                for p in P for i in range(len(p)+1)],
	                  nums, [[]])


	def permute(self, nums):
    	return list(itertools.permutations(nums))


    def permute(self, nums):
    	return map(list, itertools.permutations(nums))