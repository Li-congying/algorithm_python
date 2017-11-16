def houserobber(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = nums[0]
    choices = [-1] * (n + 1)
    choices[1] = -1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1]
        choices[i] = i - 1
        if dp[i] < dp[i - 2] + nums[i - 1]:
            dp[i] = dp[i - 2] + nums[i - 1]
            choices[i] = i - 2

    print dp[n]
    choice = n
    ret = []
    while choice != -1:
        if choices[choice] == choice - 2:
            ret.append(nums[choice - 1])
        choice = choices[choice]
    return ret[::-1]




def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    last_index = []
    #cur_index = []
    max_list = [nums[0]]
    cur_index = [0]
    for i in range(1, len(nums)):
        if i == 1:
            max_list.append(max(nums[0], nums[1]))
            if nums[1] > nums[0]:
                last_index = cur_index
                cur_index = [i]
            else:
                last_index = cur_index
        else:
            if max_list[i-1] > nums[i] + max_list[i-2]:
                last_index = cur_index
                max_list.append(max_list[i - 1])
            else:
                temp = cur_index
                last_index.append(i)
                cur_index = last_index
                last_index = temp
                max_list.append(nums[i] + max_list[i-2])
        print i, nums[i], last_index, cur_index

    return max_list[-1], cur_index

print houserobber([4, 3, 2, 1, 3, 2, 4])
print rob([4, 3, 2, 1, 3, 2, 4])
#print  houserobber([4, 4, 3, 1, 5, 6, 4])
#print rob([4, 4, 3, 1, 5, 6, 4])
