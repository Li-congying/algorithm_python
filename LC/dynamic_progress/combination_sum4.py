nums = [1,2,4]
target = 32
def c_b_4(nums , n):
    dp = {i:0 for i in range(0, n+1)}
    dp[0] = 1
    for num in nums:
        for t in dp:
            if num + t <= target:
                dp[num+t] += dp[t]


    print dp

#c_b_4(nums, target)
        #for t in dp:

def combinationSum4(nums, target) :
    nums.sort()
    dp = {i: 0 for i in range(0, target + 1)}
    dp[0] = 1
    for i in range(1,target+1):
        for n in nums:
            if n <= i:
                dp[i] += dp[i-n]
            else:
                break
    print dp[target]


combinationSum4(nums, target)


