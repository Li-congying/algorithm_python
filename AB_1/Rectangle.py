# You have a plain with lots of rectangles on it, find out how many of them intersect.
# solved by double loop + union find
# problem: several rectangles join a group, not necessarily mutual overlapping

def is_overlapping(a, b):
    x00, x01 = a[0][0], a[1][0]
    x10, x11 = b[0][0], b[1][0]
    y00, y01 = a[0][1], a[1][1]
    y10, y11 = b[0][1], b[1][1]

    return not ((x00 > x11 or x01 < x10) or (y00 > y11 or y01 < y10))


def rectangleoverlapping(rects):
    """
    rects: [[(x0,y0),(x1,y1)], ... ]
    """
    n = len(rects)
    arr = range(n)

    def find(a):
        if arr[a] != a:
            arr[a] = find(arr[a])
        return arr[a]

    def union(a, b):
        pa, pb = find(a), find(b)
        #print pa, pb
        if pa != pb:
            arr[pa] = pb
            return 1
        return 0

    num_connected = n
    for i in range(n):
        for j in range(i + 1, n):
            #print i, j,arr
            if is_overlapping(rects[i], rects[j]):
                num_connected -= union(i, j)
            #print i, j, arr
    return num_connected


print  rectangleoverlapping([[(0, 0), (3, 3)], [(0, 0), (1, 1)], [(2,2), (3,3)]])
#assert rectangleoverlapping([[(0, 0), (2, 2)], [(1, 1), (3, 3)], [(4, 4), (6, 6)], [(5, 5), (7, 7)]]) == 2


def find_intersect_num(rectangles):
    roots = {i: i for i in xrange(len(rectangles))}
    num_intersection = 0
    for i in xrange(len(rectangles)):
        for j in xrange(i):
            if is_overlapping(rectangles[i], rectangles[j]):
                i_root = find(i, roots)
                j_root = find(j, roots)
                if i_root != j_root:
                    roots[j_root] = i_root
                    num_intersection += 1
            print roots

    return num_intersection
def find(i, root):
    while i != root[i]:
        root[i] = root[root[i]]
        i = root[i]
    return i

def is_intersect(r1, r2):
    return r1[0][0] < r2[0][0] < r1[1][0] and r1[0][1] < r2[0][1] < r1[1][1] or \
r1[0][0] < r2[1][0] < r1[1][0] and r1[0][1] < r2[1][1] < r1[1][1]


print find_intersect_num([[(0, 0), (3, 3)], [(0, 0), (1, 1)], [(2,2), (3,3)]])
rectangles = [[(0, 0), (3, 3)], [(0, 0), (1, 1)],[(2,2), (3,3)]]
print rectangleoverlapping(rectangles)
# print rectangleoverlapping(rectangles)
# print find_intersect_num(rectangles)



# def is_overlap(r1, r2):
#     r1_l_x, r1_l_y = r1[0][0], r1[1][0]
#     r1_r_x, r1_r_y = r1[1][0], r1[1][1]
#     r2_l_x, r2_l_y = r2[0][0], r2[1][0]
#     r2_r_x, r2_r_y = r2[1][0], r2[1][1]
#
#     return not ((r1_l_x > r2_r_x or r1_r_x < r2_l_x) or (r1_l_y > r2_r_y or r1_r_y < r2_l_y))


