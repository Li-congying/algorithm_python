from heapq import *


def meetingrooms(ints, t1, t2):
    ends = []
    ret = []
    s, e = ints[0], ints[1]
    last = 0

    for s, e in ints:
        while ends and s > ends[-1]:
            last = heappop(ends)

        # compare [t1,t2] with [last, s], get overlapping part
        if not ends:
            if not (t1 >= s or t2 <= last):
                ret.append((max(t1, last), min(t2, s)))
                if t2 <= s:
                    return ret

        heappush(ends, e)

    while ends:
        last = heappop(ends)
    if t2 > last:
        ret.append((max(t1, last), t2))
    return ret


meetingrooms([[2, 3], [5, 6], [8, 9]], 0, 10)
# assert meetingrooms([[1, 6], [2, 5], [7, 8]], 5, 7) == [(6, 7)]  # overlapping as well as new
# assert meetingrooms([[2, 3], [5, 6], [8, 9]], 0, 10) == [(0, 2), (3, 5), (6, 8), (9, 10)]  # cover all
# assert meetingrooms([[2, 6], [8, 9]], 2, 3) == []  # no free room
# assert meetingrooms([[2, 7], [3, 8]], 8, 8) == []  # no free room
# assert meetingrooms([[2, 7], [3, 8]], 0, 8) == [(0, 2)]  # free at beginning


busy_time = [[3, 4], [2, 7], [7, 9], [2, 5], [0, 11]]
meeting_time = [1, 11]


def getMeetingTime(busy_time, meeting_time):
    result = [meeting_time]
    i = 0
    while i < len(busy_time) and len(result):
        stime = busy_time[i][0]
        etime = busy_time[i][1]

        j = 0
        cur_length = len(result)
        while j < cur_length:
            t_r = result[0]
            del (result[0])
            if stime >= t_r[1] or etime <= t_r[0]:
                result.append(t_r)
            else:
                if t_r[0] < stime:
                    result.append([t_r[0], stime])
                if t_r[1] > etime:
                    result.append([etime, t_r[1]])
            j += 1

        # print result
        i += 1

    return result


#print getMeetingTime(busy_time, meeting_time)

def getMeetingTime(busy_time, meeting_time):
    starts = {}
    ends = {}
    min_v = float('+inf')
    max_v = float('-inf')
    for lt in busy_time:
        starts[lt[0]] = starts.get(lt[0], 0) + 1
        ends[lt[1]] = ends.get(lt[1], 0) + 1
        min_v = min(lt[0], min_v)
        max_v = max(lt[1], max_v)

    result = []
    cur_busy = 0
    s = 0
    for i in range(min(min_v, meeting_time[0]),  meeting_time[1]+1):

        if i in starts:
            if cur_busy == 0:
                e = i
                if e > meeting_time[0] and s < meeting_time[1]:
                    result.append([max(s, meeting_time[0]), min(e, meeting_time[1])])
            cur_busy += starts[i]


        if i in ends:
            if cur_busy and cur_busy-ends[i] == 0:
                s = i
            cur_busy -= ends[i]

        if cur_busy == 0 and i ==  meeting_time[1]:
            e = i
            if e > meeting_time[0] and s < meeting_time[1]:
                result.append([max(s, meeting_time[0]), min(e, meeting_time[1])])


        print i, cur_busy

    return result

busy_time = [[5, 10]]
meeting_time = [0, 15]
print getMeetingTime(busy_time, meeting_time)

