'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for bracket in s:
            if bracket in dic.values():
                stack.append(bracket)
            elif bracket in dic:
                if stack == [] or stack.pop() != dic[bracket]:
                    return False
            else:
                return False
        return stack == []