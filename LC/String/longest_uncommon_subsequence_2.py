'''
Given a list of strings, you need to find the longest uncommon subsequence among them. 
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and 
this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing 
the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string 
is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. 
If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
'''
class Solution(object):

    def uncommon(self, str_1, str_2):
        i = 0
        j = 0
        while i < len(str_1):
           if str_1[i] == str_2[j]:
               j += 1
           if j == len(str_2):
               break
           i += 1
        return j != len(str_2)


    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        len_str = {}
        for str in strs:
            if len(str) not in len_str:
                len_str[len(str)] = {}
            len_str[len(str)][str] = len_str[len(str)].get(str, 0) + 1

        keys = sorted(len_str.keys(), reverse=True)
        large_keys = []
        for key in keys:
            for str in len_str[key]:
                if len_str[key][str] == 1:
                    uncommon = True
                    for large_key in large_keys:
                        for l_str in len_str[large_key]:
                            if not self.uncommon(l_str, str):
                                uncommon = False
                                break
                        if not uncommon:
                            break
                    if uncommon:
                        return key

            large_keys.append(key)

        return -1



obj = Solution()
print obj.findLUSlength(["ac", "abc", "abc", "abce", "abce"])
