'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s
        base_count = numRows + numRows - 2
        result = ''
        mid_base = base_count
        for i in range(min(numRows, len(s))):
            start = i
            while start < len(s):
                result += s[start]
                if mid_base != base_count and start + mid_base < len(s):
                    result += s[start + mid_base]
                #print start, base_count, s[start], result, mid_base
                start += base_count
            mid_base -= 2
            if mid_base == 0:
                mid_base = base_count

        return result

obj = Solution()
print obj.convert("AB", 1)
