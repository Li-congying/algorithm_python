input = [0.32, 1.30, 3.37, 0.65, 0.95, 2.30]
total = 2.57
def menuOrder(input, total):
    input.sort()
    result = []
    def helper(input, index, total, target, result):
        if input[index] > target:
            return
        lt.append(input[index])
        total += input[index]
        if total*100 == target*100:
            result.append(lt)
            return
        for i in range(index + 1, len(input)):
            if total + input[i] < target:
                helper(input, i, total, target, lt[:], result)
            if (total + input[i]) * 100 == target * 100:
                lt.append(input[i])
                #print 'match', set_
                result.append(lt)
                return

    for i in range(len(input)):
        lt = []
        helper(input, i, 0, total, lt, result)
        if len(result):
            return result[0]
            break


print menuOrder(input, 0)