'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

'''
from heapq import *
class Solution:
    def largestNumber(self, nums):
        '''
        :param nums: List
        :return: string
        '''
        def comp(a, b):
            if int(str(a) + str(b)) < int(str(b) + str(a)):
                return 1
            else:
                return -1
        nums.sort(comp)
        return ''.join([str(num) for num in nums]) if nums[0] != 0 else 0


obj = Solution()
print obj.largestNumber([3, 30, 34, 5, 9])
