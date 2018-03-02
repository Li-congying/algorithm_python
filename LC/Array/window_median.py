'''
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from 
the very left of the array to the very right. You can only see the k numbers 
in the window. Each time the sliding window moves right by one position. 
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
'''
from heapq import *
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        def insetToHeap(num, max_heap, min_heap):
            print 'p', num, max_heap, min_heap
            if len(max_heap) == len(min_heap):
                if not max_heap or num < min_heap[0]:
                    heappush(max_heap, -num)
                else:
                    heappush(max_heap, -heappop(min_heap))
                    heappush(min_heap, num)
            else:
                if num < -max_heap[0]:
                    heappush(min_heap, -heappop(max_heap))
                    heappush(max_heap, -num)
                else:
                    heappush(min_heap, num)
            print 'pp', num, max_heap, min_heap

        min_heap = []
        max_heap = []
        for num in nums[0:k]:
            insetToHeap(num, max_heap, min_heap)

        result = []
        for i in range(k, len(nums) + 1):
            #print 'start', [-key for key in max_heap], min_heap
            if k % 2 == 1:
                result.append(min_heap[0] * 1.0 if len(min_heap) > len(max_heap) else max_heap[0] * -1.0)
            else:
                result.append((min_heap[0] - max_heap[0])/2.0)
            if i < len(nums):
                print nums[i], nums[i-k]
                #print 'insert', nums[i]
                if nums[i] == nums[i-k]:
                    continue
                if nums[i-k] <= - max_heap[0]:
                    for j in range(len(max_heap)):
                        if nums[i-k] == -max_heap[j]:
                            break
                    # if len(max_heap) > len(min_heap):
                    #
                    if nums[i] < min_heap[0]:
                        max_heap[j] = -nums[i]
                    else:
                        max_heap[j] = -heappop(min_heap)
                        heappush(min_heap, nums[i])
                    #del(max_heap[j])
                    #_shift
                    heapify(max_heap)
                else:
                    for j in range(len(min_heap)):
                        if nums[i-k] == min_heap[j]:
                            break
                    if nums[i] > -max_heap[0]:
                        min_heap[j] = nums[i]
                    else:
                        min_heap[j] = -heappop(max_heap)
                        heappush(max_heap, -nums[i])
                    heapify(min_heap)
                print nums[i], max_heap,min_heap
                # if len(min_heap) > len(max_heap) :
                #     heappush(max_heap, -heappop(min_heap))
                #
                # insetToHeap(nums[i], max_heap, min_heap)
                #print 'end', [-key for key in max_heap], min_heap

        return result


obj = Solution()
print obj.medianSlidingWindow([1,3,-1,-3,5,3,6,7]
,3)
#
# '''
# [7,0,3,9,9,9,1,7,2,3]
# 6
# '''
#[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]




