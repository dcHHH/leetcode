'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'AEIOUaeiou'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while s[i] not in vowels and i < j:
                i += 1
            while s[j] not in vowels and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j -1
        return ''.join(s)


def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)