list = [1,4,5,6,8]
k = 2
target = 8

def kSum(list, k ,target):
    dp = {key :[0 for i in range(target+1)] for key in range(1, k+1)}
    #print dp
    for num in range(len(list)):
        if list[num] > target:
            break
        print num,list[num]
        max_k = min(num+1, k) + 1
        for kk in range(2, max_k)[::-1]:
            for t in range(target+1)[::-1]:
                if t >= list[num]:
                    dp[kk][t] += dp[kk-1][t-list[num]]
                else:
                    break
        dp[1][list[num]] = 1
        print dp

    return dp[k][target]





def k_sum(list, k, target):
    dp = {key:{t:0 for t in range(0, target+1)} for key in range(1, k+1)}
    for i in range(len(list)):
        num = list[i]
        if num > target:
            continue
        max_k = min(k, i+1)
        for kk in range(2, max_k+1)[::-1]: # cal 1 to mak_k's sum group
            for t in range(target+1)[::-1]: # cal 0 to target sum
                if num > t:
                    continue

                dp[kk][t] += dp[kk-1][t-num]
                if kk == 3:
                    print 'kk', kk, t, num, dp[kk-1][t-num], dp[kk][t]

        dp[1][num] = 1

    #print dp
    return dp[k][target]


# for i in range(2,2):
#     print 'i', i


list = [1,2,3,4,5,6,7]
k = 2
target = 8
print k_sum(list, 3, 10)