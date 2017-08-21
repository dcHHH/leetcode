'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        t2, t3, t5 = 0, 0, 0
        while len(ugly) < n:
            while ugly[t2] * 2 <= ugly[-1]:
                t2 += 1
            while ugly[t3] * 3 <= ugly[-1]:
                t3 += 1
            while ugly[t5] * 5 <= ugly[-1]:
                t5 += 1
            ugly.append(min(ugly[t2] * 2, ugly[t3] * 3, ugly[t5] * 5))
        return ugly[-1]