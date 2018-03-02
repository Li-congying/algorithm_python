'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
'''
import math
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        str_ = str(N)
        i = 0
        while i < len(str_) - 1:
            if str_[i] > str_[i+1]:
                break
            i += 1

        if i == len(str_) - 1:
            return N

        if str_[i] == '1':
            r_str = '9' * (len(str_) - 1)
        else:
            while i >= 0:
                if str_[i] > str_[i-1]:
                    break
                i -= 1
            i = max(i, 0)
            r_str = str_[:i] + str(int(str_[i])-1) + (len(str_) - i -1) * '9'

        return int(r_str)

obj = Solution()
print obj.monotoneIncreasingDigits(768887)

