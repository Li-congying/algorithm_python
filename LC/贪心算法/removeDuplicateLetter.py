'''
Given a string which contains only lowercase letters, 
remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = []
        for i in range(len(s)):
            list.append((s[i], i))

        new_list = sorted(list, key=lambda x:x[0], reverse=True)
        print new_list
        #print list


obj = Solution()
obj.removeDuplicateLetters('bcacb')