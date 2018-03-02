'''
Count Different Palindromic Subsequences
Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
'''


class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        c_count = {k:0 for k in 'abcd'}
        for i in range(len(S)):
            c_count[S[i]].append(i)

        self.dp = [[0] * len(S)] * len(S)
        def helper(start, end):
            if start > end:
                return 0
            if self.dp[start][end] :
                return self.dp[start][end]
            cur_s = S[start]


        # size = len(S)
        # next = [{k: -1 for k in 'abcd'} for x in range(size + 1)]
        # prev = [{k: -1 for k in 'abcd'} for x in range(size + 1)]
        # for x in range(size):
        #     for k in 'abcd':
        #         if S[x] == k:
        #             prev[x][k] = x
        #         else:
        #             prev[x][k] = prev[x - 1][k]
        #
        # print prev
        #
        # for x in range(size - 1, -1, -1):
        #     for k in 'abcd':
        #         if S[x] == k:
        #             next[x][k] = x
        #         else:
        #             next[x][k] = next[x + 1][k]
        #
        # print next
        #
        # dmap = [[0] * (size + 1) for x in range(size + 1)]
        #
        # def solve(i, j):
        #     if i > j: return 0
        #     if dmap[i][j]: return dmap[i][j]
        #     ans = 0
        #     for k in 'abcd':
        #         ii, jj = next[i][k], prev[j][k]
        #         if ii < 0: continue
        #         if ii < jj: ans += 1
        #         if ii <= j: ans += solve(ii + 1, jj - 1) + 1
        #     dmap[i][j] = ans % (10 ** 9 + 7)
        #     return dmap[i][j]
        #
        # return solve(0, size - 1)

obj = Solution()
obj.countPalindromicSubsequences('bccb')