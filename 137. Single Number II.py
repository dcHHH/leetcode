'''
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one
#Actually, this approach can be generalized for the case that each number appears 5 times except one:

class Solution(object):
    def singleNumber(self, nums):
        one = two = three = four = 0
        for x in nums:
            one, two, three, four, five = one ^ x, two | (one & x), three | (two & x), four | (three & x), four & x
            one, two, three, four = one & ~three & ~five, two & ~three, three & ~four, four & ~five
        return one
#If each number appears 5 times except that one number appears only 3 times, return three will be the result
