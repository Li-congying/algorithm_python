'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.        
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == float('-inf') and divisor == 1) or dividend == float('inf'):
            return float('inf')
        sign = True
        if (divisor > 0 and dividend < 0) or (divisor<0 and dividend>0):
            sign = False
        divisor = abs(divisor)
        dividend = abs(dividend)
        result = 0
        count = 1
        while dividend > 0:
            if dividend - divisor >= 0:
                dividend = dividend - divisor
                result += count
                divisor = divisor << 1
                count = count << 1
            else:
                divisor = divisor >> 1
                count = count >> 1
                if count == 0:
                    break
            #print dividend, divisor, result

        return result if sign else -result

    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a, b = abs(dividend), abs(divisor)
        ret, c = 0, 0

        while a >= b:
            c = b
            i = 0
            while a >= c:
                a -= c
                ret += (1 << i)
                i += 1
                c <<= 1

        if sign:
            ret = -ret
        return min(max(-2147483648, ret), 2147483647)



obj = Solution()
# print (0<<1)+1
print obj.divide(9, -9)

