#Given an array of integers, every element appears twice \
#except for one. Find that single one.
#Your algorithm should have a linear runtime complexity


class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)        