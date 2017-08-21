'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[:2] = [False, False]
        for i in range(2, int((n -1 ) ** 0.5) + 1):
            if primes[i]:
                primes[i ** 2:: i] = [False] * len(primes[i ** 2:: i])
        return sum(primes)