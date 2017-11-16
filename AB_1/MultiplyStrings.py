class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        if num1[0] not in ['+', '-']:
            num1 = '+'+num1
        if num2[0] not in['+', '-']:
            num2 = '+'+num2
        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        total = 0
        for index in range(len(num2)-1, 0, -1):
            n_2 = int(num2[index])
            base = 0
            out_string = ''
            for j in range(len(num1)-1, 0, -1):
                n_1 = int(num1[j])
                mul = n_2 * n_1 + base
                out_string = str(mul%10) + out_string
                base = mul / 10

            if out_string == '':
                out_string = 0
            else:
                out_string = int(str(base)+out_string)

            total += out_string * (10**(len(num2)-index-1))

        if num1[0] != num2[0]:
            return '-' + str(total)
        else:
            return str(total)

s = Solution()
print s.multiply('99', '-8')
print 98*8