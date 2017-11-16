'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hash_map = {}
        result = []
        for n in nums:
            if not hash_map:
                hash_map[str(n)] = 1
                result.append([n])
            else:
                temp = []
                while result:
                    m = result.pop()
                    for i in range(len(m)+1):
                        nxt = m[:i] + [n] + m[i:]
                        hash_str = ''
                        for num in nxt:
                            hash_str += str(num)
                        if hash_str not in hash_map:
                            hash_map[hash_str] = 1
                            temp.append(nxt)
                result = temp

        return result

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            newRes = []
            for l in res:
                for i in xrange(len(l) + 1):
                    # insert the number at all possible indices in the array
                    newRes.append(l[:i] + [num] + l[i:])
                    # its a duplicate if num already exists in l at this index
                    if i < len(l) and l[i] == num:
                        break
            res = newRes
        return res
obj = Solution()
print obj.permuteUnique([1,1,2,2])
