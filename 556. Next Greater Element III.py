'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = str(n)
        for i in reversed(range(len(num) - 1)):
            if num[i] < num[i+1]:
                t = list(num[i:])
                for j in reversed(range(1, len(t))):
                    if t[j]>t[0]:
                        t[0], t[j] = t[j], t[0]
                        rest = reversed(t[1:])
                        res = int(num[:i] + t[0] + ''.join(rest)) 
                        return res if res <= (2**31-1) else -1 
        return -1
                