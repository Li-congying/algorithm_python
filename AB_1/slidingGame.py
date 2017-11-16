def get_dst(num, m):
    if num == 0:
        return (m-1, m-1)
    return ((num-1)/m, (num-1)%m)

def get_distance(board):
    m = len(board)
    distance = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '0':
                dst = get_dst(int(board[i][j]), m)
                distance += abs(i-dst[0]) + abs(j-dst[1])
            #print i, j, board[i][j], dst, abs(i-dst[0]) + abs(j-dst[1])

    return distance

def serialize(board):
    res = [i for r in board for i in r]
    return ",".join(res)



from heapq import *

def slidingPuzzle(board, x, y):
    close_list = set()
    queue = [[board, get_distance(board),  x, y]]
    moves = [ [1, 0], [-1, 0], [0, -1], [0,1]]
    width = len(board)
    close_list.add(serialize(board))
    index = 1
    while queue:
        # key = queue.keys()[0]
        # q = queue[0]
        # del(queue[0])
        q = heappop(queue)
        if q[1] == 0:
            return True
        print q[0]
        #print len(close_list)
        x = q[2]
        y = q[3]
        for mv in moves:
            cur = [row[:] for row in q[0]]
            #print 'cur', cur, q[0]
            if 0 <=x+mv[0] < width and  0 <=y+mv[1] < width:
                cur[x][y] = cur[x+mv[0]][y+mv[1]]
                cur[x + mv[0]][y + mv[1]] = '0'
                sl = serialize(cur)
                if sl not in close_list :
                    if sl not in queue :
                        nxt = [cur, get_distance(cur), x + mv[0], y + mv[1]]
                        close_list.add(serialize(cur))
                        heappush(queue, nxt)

    return False


#print get_distance([['1', '0', '3'], ['4', '2', '5'], ['7', '8', '6']])

#print slidingPuzzle([["1","2","3"],["4","5","6"],["8","7","0"]], 2, 2)

lt = [["1","2","3"],["4","0","5"],["7","8","6"]]
#print slidingPuzzle(lt, 2, 2)

#lt = [["1","2","3"],["4","0","5"],["7","8","6"]]


from heapq import *
import copy


def slidingpuzzle(cur, x, y):
    m = len(cur)

    def serialize(cur):
        res = [c for row in cur for c in row]
        return ','.join(res)

    def manhattan(cur, target):
        cur = serialize(cur).split(',')
        target = serialize(target).split(',')
        dist = 0
        for i in range(len(cur)):
            x0, y0 = i / m, i % m
            idx = target.index(cur[i])
            x, y = idx / m, idx % m
            dist += abs(x0 - x) + abs(y0 - y)
        return dist

    target = [[0] * m for _ in range(m)]
    e = 1
    for i in range(m):
        for j in range(m):
            target[i][j] = str(e)
            e += 1
    target[m - 1][m - 1] = "0"

    visited = set()
    visited.add(serialize(cur))
    mdist = manhattan(cur, target)
    #print mdist, cur, target
    q = [(mdist, cur, x, y)]
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    index = 1
    while q:
        mdist, cur, x, y = heappop(q)
        print cur
        for d in dirs:
            x0, y0 = x + d[0], y + d[1]
            if 0 <= x0 < m and 0 <= y0 < m:
                next = copy.deepcopy(cur)
                next[x0][y0], next[x][y] = next[x][y], next[x0][y0]
                if serialize(next) == serialize(target):
                    return True
                if serialize(next) not in visited:
                    visited.add(serialize(next))
                    heappush(q, (manhattan(next, target), next, x0, y0))

        #index += 1
        # if index > 4:
        #     break

    return False

print slidingPuzzle([["1","2","3"],["4","5","6"],["8","7","0"]], 2, 2)
#assert slidingpuzzle([["1", "2", "3"], ["4", "0", "5"], ["7", "8", "6"]], 1, 1) == True
#slidingpuzzle([["2", "1", "3"], ["5", "4", "8"], ["6", "7", "0"]], 2, 2)
# assert slidingpuzzle([["1", "0", "3"], ["2", "4", "5"], ["6", "7", "8"]], 0, 1) == False
# assert slidingpuzzle([["7", "0", "2"], ["8", "5", "3"], ["6", "4", "1"]], 0, 1) == False
# unsolvable, can't finish running
# print slidingpuzzle([["1","2","3","4"], ["5","6","7","8"], ["9","10","11","12"], ["13","15","14","0"]], 3,3)


# h = []
# heappush(h, [2,3,3])
# heappush(h, [1, 2,2])
# print heappop(h)




