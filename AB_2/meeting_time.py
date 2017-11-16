busy_time = [[0, 3], [5, 10], [4, 12]]
meeting_time = [1, 11]

def getMeetingTime(busy_time, meeting_time):
    start_set = {}
    end_set = {}
    min_time = float('+inf')
    # max_time = meeting_time[1]
    for s, e in busy_time:
        start_set[s] = start_set.get(s, 0) + 1
        end_set[e] = end_set.get(e, 0) + 1
        min_time = min(s, min_time)

    cur_count = 0
    start = min_time
    result = []
    for t in range(min_time, meeting_time[1] + 1):
        if t in start_set:
            if cur_count == 0 and t > start:
                result.append([start, t])
            cur_count += start_set[t]

        if t in end_set:
            cur_count -= end_set[t]
            if cur_count == 0:
                start = t

        if t == meeting_time[1] and cur_count == 0:
            result.append([start, t])
    print result

    # print start_set, end_set, min_time


getMeetingTime(busy_time, meeting_time)