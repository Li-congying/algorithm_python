def printWater(elevation, res):
    n = len(elevation)
    m = max([elevation[i] + res[i] for i in range(n)])

    grid = [[0] * n for _ in range(m)]
    for i in range(n):
        height = elevation[i] + res[i]
        for j in range(height):
            grid[m - j - 1][i] = 1

    for i in range(m):
        print '\n',
        for j in range(n):
            if grid[i][j] == 1:
                print 'x',
            else:
                print ' ',


def findnextloc(elevation, res, loc):
    n = len(elevation)
    cur = loc
    while cur >= 1 and elevation[cur - 1] + res[cur - 1] <= elevation[cur] + res[cur]:
        cur -= 1
    start = cur
    while cur < n - 1 and elevation[cur + 1] + res[cur + 1] <= elevation[cur] + res[cur]:
        if elevation[cur + 1] + res[cur + 1] < elevation[cur] + res[cur]:
            start = cur + 1
        cur += 1
    return start, cur


def fillwater(elevation, water, loc):
    n = len(elevation)
    res = [0] * n
    printWater(elevation, res)
    while water > 0:
        start, end = findnextloc(elevation, res, loc)
        # print "start={}, end={}".format(start,end)
        for i in range(start, end + 1):
            if water == 0:
                break

            res[i] += 1
            water -= 1
    printWater(elevation, res)
    print '\n'
    return res

#fillwater([1,2,3,2,1], 3, 3)

# assert )# == [0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0]
#
#
# assert fillwater([5, 4, 2, 2, 2, 3, 2, 1, 0, 1, 2, 4], 8, 5)# == [0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0]
#
# assert fillwater([5, 4, 2, 3, 2, 3, 2, 1, 0, 1, 2, 4], 8, 5)# == [0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0]
# assert fillwater([1, 2, 1], 1, 1) == [1, 0, 0]
# assert fillwater([1, 2, 1], 2, 1) == [1, 0, 1]
# assert fillwater([1, 2, 1], 3, 1) == [2, 0, 1]
# assert fillwater([1, 2, 1], 4, 1) == [2, 1, 1]

# dynamic
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 1, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 2, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 3, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 4, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 5, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 6, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 7, 5)
# fillwater([5,4,2,1,2,3,2,1,0,1,2,4], 8, 5)







def pullWater(heights, loc, water):
    water_heights = [0 for i in range(len(heights))]

    while water:
        pos = findPos(heights, water_heights, loc)
        water_heights[pos] += 1
        water -= 1
        printHeights_water(heights, water_heights)
        print '\n'


def findPos(heights, water_heights, loc):
    left = loc
    while left > 0 and heights[left - 1] + water_heights[left - 1] <= heights[left] + water_heights[left]:
        left -= 1
    if heights[left] + water_heights[left] != heights[loc] + water_heights[loc]:
        return left

    right = loc
    while right < len(heights) - 1 and heights[right + 1] + water_heights[right + 1] <= heights[right] + water_heights[
        right]:
        right += 1
    if heights[right] + water_heights[right] != heights[loc] + water_heights[loc]:
        return right
    return loc


def printHeights_water(heights, water_heights):
    height = 1
    status = True
    result = []
    while status:
        status = False
        str_ = ''
        # print height
        for i in range(len(heights)):
            if heights[i] >= height:
                str_ += '*'
                status = True
            elif water_heights[i] + heights[i] >= height:
                str_ += 'w'
                status = True
            else:
                str_ += ' '
        if status:
            result.append(str_)
            height += 1

    print "\n".join(result[::-1])


heights = [1, 2, 3, 2, 1]
# heights = [3,3,3,3,3]
loc = 3
water = 7


pullWater(heights, loc, water)




