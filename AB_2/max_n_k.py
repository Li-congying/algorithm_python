_str = "9789323"

def getMaxN_K(_str, k):

    if len(_str) == 0 or len(_str) == k:
        return 0

    start = 0
    while start < k:
        min_set = [0]
        for i in range(1,len(_str)):
            if _str[i] < _str[i-1]:
                min_set.append(i)
            else:
                break
        print min_set, i
        _str = _str[0:min_set[-1]] + _str[min_set[-1]+1:]
        start += 1

    print _str

getMaxN_K(_str, 2)