'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        rSum = [2**31] * (n - 1) + [0]
        for i in grid[::-1]:
            for j in range(n)[::-1]:
                rSum[j] = min(rSum[j: j + 2]) + i[j]
        return rSum[0]