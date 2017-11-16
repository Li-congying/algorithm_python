height = [1, 2, 3, 2, 1, 4]
loc = 2
water = 8


def fillWater(height, loc, water):
    water_height = [0 for i in range(len(height))]
    while water:
        fill_loc = findLoc(height, water_height, loc)
        print fill_loc
        water_height[fill_loc] += 1
        water -= 1
        printWater(height, water_height)
        print '\n'


def findLoc(h, w_h, loc):
    left = loc

    # print h[left-1] + w_h[left-1], h[left] + w_h[left], left-1
    while left - 1 >= 0 and h[left - 1] + w_h[left - 1] <= h[left] + w_h[left]:
        left -= 1

    # print 'left', left
    if h[left] + w_h[left] < h[loc] + w_h[loc]:
        return left

    right = loc

    while right + 1 < len(h) and h[right + 1] + w_h[right + 1] <= h[right] + w_h[right]:
        right += 1

    if h[right] + w_h[right] < h[loc] + w_h[loc]:
        return right

    return loc


def printWater(height, water):
    max_h = max([height[i] + water[i] for i in range(len(height))])

    for h in range(1, max_h + 1)[::-1]:
        str_ = ""
        for i in range(len(height)):
            if height[i] >= h:
                str_ += '*'
            elif height[i] + water[i] >= h:
                str_ += 'w'
            else:
                str_ += ' '
        print str_ + '\n'


fillWater(height, loc, water)
