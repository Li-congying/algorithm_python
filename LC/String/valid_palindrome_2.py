'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            for i in range(len(s)/2):
                if s[i] != s[len(s)-1-i]:
                    return False
            else:
                return True

        for i in range(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                new_str_1 = s[0:i]+s[i+1:]
                new_str_2 = s[0:len(s)-1-i]+s[len(s)-i:]
                print new_str_1, new_str_2
                return isPalindrome(new_str_1) or isPalindrome(new_str_2)

        return True

obj = Solution()
print obj.validPalindrome('acbbcca')