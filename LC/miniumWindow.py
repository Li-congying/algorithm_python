'''
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_window = ''
        dp = [[(0, 0) for i in range(len(s)+1)] for j in range(len(t)+1)]
        for i in range(1, len(dp)):
            is_match = False
            # for j in range(1, len(dp[i])):
            #     if(t[i-1] == s[j-1]) and not is_match:
            #         match = dp[i-1][j][1] + 1
            #         if i == 1:
            #             index = j
            #         else:
            #             index = min(dp[i-1][j][0], j)
            #
            #     else:
            #         match = dp[i-1][j][1] + dp[i][j-1][1]
            #         index = min(dp[i-1][j-1][0], dp[i][j-1][0])
            #         dp[i][j] = (index, match)
            #
            #         #index = min()
                #index = min(dp[i-1][j][0], dp[i][j-1])
                # if s[j-1] == t[i-1]:
                #     index
                #     #dp[i][j] = (i, dp[i-1][j][1] + 1)
                # else:
                    #dp[i][j] = (dp[i][j-1][0], dp[i][j-1][0] + dp[i-1][j][1])

        print dp
s = "EBANC"
t = 'ABC'
solution = Solution()
solution.minWindow(s, t)