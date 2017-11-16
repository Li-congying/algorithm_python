'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(1, len(nums)-1):
            l = i-1
            r = i+1
            total = nums[i] + nums[l] + nums[r]
            while total != 0:
                if total < 0 and r < len(nums)-1:
                    r += 1
                elif total > 0 and l > 0:
                    l -= 1
                else:
                    break
                total = nums[i] + nums[l] + nums[r]

            if nums[i] + nums[l] + nums[r] == 0:
                result.append([nums[l], nums[i], nums[r]])

        return result

obj = Solution()
print obj.threeSum([-1, 0, 1, 2, -1, -4])