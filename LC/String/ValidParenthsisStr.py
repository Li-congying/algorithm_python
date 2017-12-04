'''
Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
'''
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        comm = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            if s[i] == '*':
                comm.append(i)
            if s[i] == ')':
                if left:
                    left.pop()
                elif comm:
                    comm.pop()
                else:
                    return False

        while left:
            index_l = left.pop()
            if not comm:
                return False
            else:
                index_c = comm.pop()
                if index_c < index_l:
                    return False

        return True


obj = Solution()
print obj.checkValidString('*)')