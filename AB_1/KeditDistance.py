def getKdistanceWord( word_list, target, k):
    nodes = {}
    for word in word_list:
        node = nodes
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = {}
            node = node[word[i]]
            if i == len(word)-1:
                node['#'] = 1


    def helper(prev_dp, w, node, target, prev_str, result):
        curr_dp = [prev_dp[0] + 1]
        for i in range(len(target)):
            if target[i] == w:
                curr_dp.append(prev_dp[i])
            else:
                min_dis = min(prev_dp[i]+1, curr_dp[i]+1, prev_dp[i+1]+1)
                curr_dp.append(min_dis)
        if curr_dp[-1] <= k and '#' in node:
            result.append(prev_str+w)
        for nxt in node:
            if nxt != '#':
                helper(curr_dp, nxt, node[nxt], target, prev_str+w, result)


    result = []
    for key in nodes:
        prev_dp = [i for i in range(len(target) + 1)]
        helper(prev_dp, key, nodes[key], target, "", result)

    return result



getKdistanceWord(['abc', 'acd', 'ade', 'dc', 'a'], 'aed', 1)


def editDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    dp = [[j+i for j in range(n1+1)] for i in range(n2+1)]
    for i in range(1,n2+1):
        for j in range(1, n1+1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] +1, dp[i-1][j-1]+1)
    return dp[n2][n1]

print editDistance('abc', 'ac')


