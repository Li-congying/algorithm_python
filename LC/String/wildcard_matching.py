'''
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:

isMatch("ab", "?*")true
isMatch("aab", "c*a*b")false
'''



class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == '':
            return p == '' or p == '*'
        if p == '':
            return s == ''
        if p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        else:
            if s[0] == p[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False


    def isMatch_dp(self, s, p):
        if s == '':
            return p == '' or p == '*'
        if p == '':
            return s == ''
        dp = [[0 for _ in range(len(s)+1)] for __ in range(len(p)+1)]
        dp[0][0] = 1
        if p[0] == '*':
            for i in range(1, len(dp[0])):
                dp[0][i] = 1
        for i in range(1, len(dp)):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0]
        print dp[0]
        for i in range(1,len(dp)):
            for j in range(1, len(dp[0])):
                if p[i-1] == '?' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-1] or dp[i][j-1]

            print dp[i]
        return dp[-1][-1] == 1


    def isMatch2(self, s, p):
        index_p, index_s = 0, 0
        m_p, m_s = -1, -1
        while index_s < len(s):
            print index_p, p[index_p], index_s, s[index_s], m_p, m_s
            if index_p < len(p) and (p[index_p] == s[index_s] or p[index_p] == '?'):
                index_p += 1
                index_s += 1
            elif index_p < len(p) and p[index_p] == '*':
                m_p = index_p
                m_s = index_s
                index_p += 1
            elif m_p != -1:
                index_p = m_p + 1
                index_s = m_s + 1
                m_s += 1
            else:
                return False


        while index_p < len(p) and p[index_p] == '*':
            index_p += 1
        return index_p == len(p)





obj = Solution()
#print obj.isMatch2("abefcdgiescdfimde", "ab*cd?i*de")
print obj.isMatch2("zzacabz","*a?b*")
# print obj.isMatch2('a', '*?*')
# print obj.isMatch2('hp', '**hp')
# print obj.isMatch2("aab","c*a*b")

