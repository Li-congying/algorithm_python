'''
with A = "abcd" and B = "cdabcdab"
Return 3
'''
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        base = len(B)/len(A) + 1
        extra = base+1
        to_comp = A*extra
        result = False
        for i in range(len(A)):
            if to_comp[i:i+len(B)] == B:
                result = True
                break
        # print i
        if result:
            return   (i+len(B)-1)/len(A)+1
        else:
            return -1

obj = Solution()
print obj.repeatedStringMatch('aa', 'aaaaa')