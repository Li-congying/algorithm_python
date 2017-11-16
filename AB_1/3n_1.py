def maxstep(a, b):
    # steps = [0] * b
    # steps[1] = 1
    # steps[2] = 2
    step = {}
    step[1] = 0
    step[2] = 1
    for i in range(3, b):
        j = i
        # simulate
        cnt = 0
        while j != 1:
            print j
            if j & 1 == 0:
                j >>= 1
            else:
                j = 3 * j + 1
            cnt += 1
            # only get cache when <i
            if j < i:
                print i, j, cnt
                step[i] = step[j] + cnt
                break


    print step
    return step



maxstep(1, 5)
# assert maxstep(11, 12) == 15
# assert maxstep(27, 28) == 112