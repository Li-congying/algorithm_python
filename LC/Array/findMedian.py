'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        k = (m + n - 1)/2
        test = sorted(nums1 + nums2)
        #print test,len(test), test[k], test[k+1]
        while k > 0:
            print k, k/2
            remove = k / 2 if k / 2 > 0 else 1
            if len(nums1) < (k/2 + 1):
                nums2 = nums2[remove:]
            elif len(nums2) < (k/2 + 1):
                nums1 = nums1[remove:]
                print nums1, k/2
            elif nums1[k/2] < nums2[k/2] :
                nums1 = nums1[remove:]
            elif len(nums2) < k/2 or nums1[k/2] > nums2[k/2]:
                nums2 = nums2[remove:]
            else:
                #left_min = nums1[k/2]
                nums1 = nums1[k/2:]
                nums2 = nums2[k/2:]
                k -= (k/2)*2
                break
            k -= remove

            print nums1, nums2, k
            #break

        min_list = nums1[0:2] + nums2[0:2]
        min_list.sort()
        print min_list
        if (m+n)%2 == 1:
            return min_list[0]
        else:
            return (min_list[0+k] + min_list[1+k])/2.0







obj = Solution()
print obj.findMedianSortedArrays([2], [3,4])





    # def median(A, B):
    #     m, n = len(A), len(B)
    #     if m > n:
    #         A, B, m, n = B, A, n, m
    #     if n == 0:
    #         raise ValueError
    #
    #     imin, imax, half_len = 0, m, (m + n + 1) / 2
    #     while imin <= imax:
    #         i = (imin + imax) / 2
    #         j = half_len - i
    #         if i < m and B[j-1] > A[i]:
    #             # i is too small, must increase it
    #             imin = i + 1
    #         elif i > 0 and A[i-1] > B[j]:
    #             # i is too big, must decrease it
    #             imax = i - 1
    #         else:
    #             # i is perfect
    #
    #             if i == 0: max_of_left = B[j-1]
    #             elif j == 0: max_of_left = A[i-1]
    #             else: max_of_left = max(A[i-1], B[j-1])
    #
    #             if (m + n) % 2 == 1:
    #                 return max_of_left
    #
    #             if i == m: min_of_right = B[j]
    #             elif j == n: min_of_right = A[i]
    #             else: min_of_right = min(A[i], B[j])
    #
    #             return (max_of_left + min_of_right) / 2.0














