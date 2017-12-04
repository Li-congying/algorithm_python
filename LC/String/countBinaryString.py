'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
 "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        count = 0
        prevC = 0
        currC = 0
        prev = s[0]
        for letter in s:
            if letter == prev:
                currC += 1
            else:
                prev = letter
                prevC = currC
                currC = 1
                
            if currC <= prevC:
                count += 1
                
        return count 
        '''

        split = []
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                split.append(i)

        result = 0
        print split
        while split:
            cur_pos = split.pop(0)
            result += 1
            right = cur_pos + 1
            left = cur_pos - 2
            #print s[cur_pos-1:cur_pos+1]
            while right < len(s) and left >= 0 and s[right] == s[cur_pos] and s[left] == s[cur_pos-1]:
                print left, right, s[left:right+1]
                right += 1
                left -= 1
                result += 1


        print result

obj = Solution()
obj.countBinarySubstrings("1100100110")