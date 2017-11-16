'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        hash_table = {}
        for num in nums:
            hash_table[num] = 1
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            end = start
            while end + 1 in hash_table:
                end += 1
            if start < end:
                result.append(str(start) + "->" + str(end))
            else:
                result.append(str(start))
            i += (end - start + 1)

        return result

obj = Solution()
print obj.summaryRanges([0,2,3,4,5,6,7,8,9])