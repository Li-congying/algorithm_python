'''
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
s = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
s = "aaabc", k = 3 

Answer: ""

It is not possible to rearrange the string.
Example 3:
s = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.
'''
from heapq import *
class Solution(object):

    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        word_counts = {}
        for i in s:
            word_counts[i] = word_counts.get(i, 0) + 1

        h_q = []
        for word in word_counts:
            heappush(h_q, (-word_counts[word], word))

        result = ""
        temp_list = []
        while h_q:
            iter_time = min(len(h_q), k)
            for i in range(iter_time):
                count, word = heappop(h_q)
                count += 1
                result += word
                temp_list.append((count, word))
            if len(temp_list) < k:
                break
            else:
                while temp_list:
                    item = temp_list.pop(0)
                    if item[0] < 0:
                        heappush(h_q, item)

        if len(result) < len(s):
            return ""
        else:
            return result






obj = Solution()
print obj.rearrangeString('aaaa', 3)
