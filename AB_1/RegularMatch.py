def regularMatch(s, p):
    if p == '':
        return s == ''
    dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
    dp[0][0] = True
    for i in range(len(dp)):
        for j in range(1, len(dp[i])):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j - 2] or (i > 0  and  (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
            else:
                dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
            #print  j, p[j-1], dp[i]


    return dp[-1][-1]

#print regularMatch('aaab', 'a*b')



def regularMatch2(s, p):

    if p == '':
        return s == ''

    if len(p) >= 2 and p[1] == '*':

        if len(s) and (s[0] == p[0] or p[0] == '.'):
            return regularMatch2(s[1:], p)
        else:
            return regularMatch2(s, p[2:])

    elif len(s) and (s[0] == p[0] or p[0] == '.'):
        return regularMatch2(s[1:], p[1:])
    else:
        return False

print regularMatch2('abc', 'a.*')

