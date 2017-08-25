'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = []
        while n > 0:
            ans.append(chr((n - 1) % 26  + ord('A')))
            n = (n -1 ) / 26
        return ''.join(ans[::-1])