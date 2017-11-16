def helper(x,y,iter):
    if iter==0: return 1
    origin = 2**(iter-1)
    steps = 4**(iter-1)
    print 'aaa', x, y, iter
    if x<origin and y<origin:
        return helper(y,x,iter-1)
    elif x<origin and y>=origin:
        return steps+helper(x,y-origin, iter-1)
    elif x>=origin and y>=origin:
        return steps*2+helper(x-origin, y-origin, iter-1)
    else:
        return steps*3+helper(origin-1-y, origin-1-(x-origin), iter-1)
    return 0

def hilbertcurve(x,y,iter):
    return helper(x,y,iter)

# assert hilbertcurve(0,0,1)==1
# assert hilbertcurve(0,0,2)==1
# assert hilbertcurve(1,1,1)==3
# assert hilbertcurve(2,2,2)==9
# assert hilbertcurve(3,0,2)==16

# print hilbertcurve(1,0,2), hilbertcurve(1,1,2), hilbertcurve(0,1,2),  hilbertcurve(0,0,1)
# print hilbertcurve(0,2,2), hilbertcurve(1,2,2), hilbertcurve(1,3,2),  hilbertcurve(0,3,2)
# # print hilbertcurve(2,2,2), hilbertcurve(2,3,2), hilbertcurve(3,3,2),  hilbertcurve(3,2,2)
#
# #print 1<<1


def hilberCurve(x, y, k):
    print x, y, k
    if x == 0 and y == 0:
        return 1
    step = 4**(k-1)
    edge = 2**(k-1)
    if x < edge and y >= edge:
        total = 1 * step + hilberCurve(x, y - edge, k-1)
    if x >= edge and y >= edge:
        total = 2 * step + hilberCurve(x- edge, y-edge, k-1)
    if x <edge and y <edge:
        total = hilberCurve(y, x, k-1)
    if x >= edge and y < edge:
        total = 3 *step + hilberCurve(edge-1-y, edge-1-(x-edge), k-1)

    return total

print hilbertcurve(9,5,4)
print hilberCurve (9,5,4)
