'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        stack = []
        for i in range(len(num)):
            if stack and num[i] < stack[-1]:
                stack.pop()
            stack.append(num[i])

            print stack
        stack += num[i+1:]
        print stack





obj = Solution()
print obj.removeKdigits("10200", 3)