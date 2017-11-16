'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 if j != 0 else 1 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        print dp[-1][-1]

    def answer(self, s, t):
        d = {}
        for i, c in enumerate(t):
            pos = d.get(c, [])
            pos.append(i)
            d[c] = pos
        res = [0 for i in range(len(t))]
        for i, c in enumerate(s):
            pos = d.get(c, None)
            if pos is None:
                continue
            for t in reversed(pos):
                if t == 0:
                    res[t] += 1
                else:
                    res[t] += res[t - 1]
        return res[-1]


S = "AAABA"
T = "AAA"
obj = Solution()
obj.numDistinct(S, T)
