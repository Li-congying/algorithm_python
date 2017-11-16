'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        #temp = 0
        for i in range(len(nums)):
            if nums[i] != i + 1 and nums[i] > 0 and nums[i] <= length:
                temp = nums[i]#nums[nums[i]]
                index = i

                while temp != index+1 and temp>0 and temp<=length and temp != nums[temp-1]:
                    nums[index] = nums[nums[i]-1]
                    nums[temp-1] = temp
                    temp = nums[index]
                    print temp, index
                    #print nums
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        else:
            return length+1

    def solution(self, nums):
        n = len(nums)
        if n == 0:
            return 1
        # flag=0
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # for nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                # print(i,nums[i]-1,nums[i],nums[nums[i]-1])
                # nums[0],nums[5]=nums[5],nums[0]
                # nums[5],nums[0]=nums[0],nums[5]
                flag = nums[i] - 1
                nums[i], nums[flag] = nums[flag], nums[i]
                # nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
        # print(nums)
        nums.append(0)
        for i in range(n + 1):
            if nums[i] != i + 1:
                return i + 1
                # if nums[i]!=i:
                #     return i
        return None


obj = Solution()
print obj.firstMissingPositive([1,1])