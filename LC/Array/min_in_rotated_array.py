'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        first = 0
        end = len(nums) - 1
        #if nums[first]
        while nums[first] > nums[end] and end - first > 1:
            mid = first + (end - first)/2
            if nums[first] > nums[mid]:
                end = mid
            else:
                first = mid

        return min(nums[first], nums[end])

obj = Solution()
print obj.findMin([4,5,6,7,10,0,1,2,3])