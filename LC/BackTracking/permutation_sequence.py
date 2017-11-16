

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = [i+1 for i in range(n)]
        total = 1
        for i in range(1,n+1):
            total *= i
        result = ''
        while n:
            total = total/n
            index = (k-1)/total
            k  = k - index * total
            n = n - 1
            result += str(num[index])
            del (num[index])
            # result, index,  num, k, n

        return result

obj = Solution()
for i in range(1,25):
    print obj.getPermutation(4, i)
#print obj.getPermutation(4, 10)
