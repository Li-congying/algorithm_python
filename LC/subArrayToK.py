class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #dp = [[0 for i in range(len(nums))] for i in range(len(nums))]
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    base = nums[i]
                else:
                    base = base + nums[j]
                if base == k:
                    count += 1
        return count


s = Solution()
print s.subarraySum([1,1,1], 2)

print (1 == round(1.0))
