class Solution(object):

    def partition(self, nums, p, r):
        if p < r:
            base = nums[r]
            i = p -1
            j = p

            while j <= r:
                if nums[j] <= base:
                    i += 1
                    if i != j:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                j += 1
            return i
        else:
            return p


    def quickSort(self, nums, p, r):
        if p < r:
            i = self.partition(nums, p, r)
            self.quickSort(nums, p, i-1)
            self.quickSort(nums, i+1, r)

        return nums


    def max_heap(self, nums, i):
        if 2 * i + 1 < len(nums):
            large = i
            if 2*i + 1 < len(nums) and nums[2*i+1] > nums[large]:
                large = 2*i + 1
            if 2*i +2 <  len(nums) and nums[2*i+2] > nums[large]:
                large = 2*i + 2
            if large != i:
                temp = nums[i]
                nums[i] = nums[large]
                nums[large] = temp
                self.max_heap(nums, large)


    def heap_sort(self, nums):
        if len(nums) == 0:
            return nums
        result = []
        for i in range(len(nums)/2)[::-1]:
            self.max_heap(nums, i)
        for i in range(len(nums)):
            result.append(nums[0])
            del(nums[0])
            self.max_heap(nums, 0)
        return result


    def merge(self, nums, p, q, r):
        part_1 = nums[p:q+1]
        part_2 = nums[q+1:r+1]
        print part_1, part_2
        part_1.append(float("-inf"))
        part_2.append(float("-inf"))
        i = p
        while i <= r:
            if part_1[0] > part_2[0]:
                nums[i] = part_1[0]
                del(part_1[0])
            else:
                nums[i] = part_2[0]
                del(part_2[0])
            i += 1

    def merge_sort(self, nums, p, r):

        if p < r:
            k = (p+r)/2
            self.merge_sort(nums, p, k)
            self.merge_sort(nums, k+1, r)
            self.merge(nums, p, k, r)
            print nums
        return nums


    def count_sort(self, nums):
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        keys = count.keys()
        for i in range(1, len(keys)):
            print keys[i], keys[i-1]
            count[keys[i]] += count.get(keys[i-1], 0)
        #print count
        out_nums = [0 for i in range(len(nums))]
        for i in range(len(nums))[::-1]:
            pos = count[nums[i]]-1
            out_nums[pos] = nums[i]
            count[nums[i]] -= 1
        return out_nums









s = Solution()
#print s.quickSort([3,1,4,2,5,8,7,0], 0, 7)
#print s.heap_sort([6,1,4,2,3,5,0])

print s.merge_sort([2,5,1,3,4,6,10], 0, 6)
# print s.count_sort([7,1,3,4,2,5,10])