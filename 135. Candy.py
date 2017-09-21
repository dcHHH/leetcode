'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        need = [1] * n
        lbase, rbase = 1, 1
        for i in range(1, n):
            lbase = lbase + 1 if ratings[i] > ratings[i - 1] else 1
            need[i] = lbase
        for i in reversed(range(0, n - 1)):
            rbase = rbase + 1 if ratings[i] > ratings[i + 1] else 1
            need[i] = max(need[i], rbase)
        return sum(need)