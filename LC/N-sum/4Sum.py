'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        hash_map = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                if sum not in hash_map:
                    hash_map[sum] = []
                hash_map[sum].append((i,j))
        result = []
        for sum in hash_map:
            if 2*sum <= target and target - sum in hash_map:
                for t in hash_map[sum]:
                    for t_1 in hash_map[target-sum]:
                        if t[0] not in t_1 and t[1] not in t_1:
                            temp = []
                            for index in t + t_1:
                                temp.append(nums[index])
                            temp.sort()
                            if temp not in result:
                                result.append(temp)
                            #result.append([t[0], t[1], t_1[0], t_1[1]])
        print result

obj = Solution()
obj.fourSum([1, 0, -1, 0, -2, 2], 0)
