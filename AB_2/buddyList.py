blists = [
    ["aa", "bb", "ee", "ff"],
    ["aa", "bb", "cc", "gg"],
    ["aa", "bb", "cc", "dd"],
    ["xx", "yy", "zz", "aa"]
]
mlist = ["aa", "bb", "cc", "dd"]


def buddyList(blists, mlist):
    citys = {}
    for city in mlist:
        citys[city] = 1
    b_score = {}
    for i in range(len(blists)):
        score = 0
        for city in blists[i]:
            if city in citys:
                score += 1
        b_score[i] = score
    rcmd_list = sorted(b_score.items(), key=lambda x: x[1], reverse=True)

    print rcmd_list
    # print b_score


buddyList(blists, mlist)

