from heapq import *


def buddyList(mlist, blists):
    cities = set([c for b in blists for c in b])
    idxs = {c: list() for c in cities}

    for i, blist in enumerate(blists):
        for c in blist:
            idxs[c].append(i)

    bcounts = [0] * len(blists)

    for mc in mlist:
        if mc in idxs:
            for b in idxs[mc]:
                bcounts[b] += 1
    #print bcounts
    print bcounts
    return bcounts


def buddyListMax(mlist, blists):
    bcounts = buddyList(mlist, blists)
    return bcounts.index(max(bcounts))


def buddyListMaxK(mlist, blists, k):
    bcounts = buddyList(mlist, blists)
    minq = []
    for i, b in enumerate(bcounts):
        if len(minq) < k:
            heappush(minq, (b, i))
        elif minq[0][0] < b:
            heappop(minq)
            heappush(minq, (b, i))
    return minq


def buddyListRec(mlist, blists, k):
    """
    recommend k cities
    """
    bcounts = buddyList(mlist, blists)
    bcounts = [(c, i) for i, c in enumerate(bcounts)]
    bcounts.sort(key=lambda x: x[0], reverse=True)
    #print bcounts
    rec = set()
    for cnt, i in bcounts:
        for city in blists[i]:
            if city not in mlist:
                rec.add(city)
                if len(rec) == k:
                    return rec
    return rec


blists = [
    ["aa", "bb", "ee", "ff"],
    ["aa", "bb", "cc", "gg"],
    ["aa", "bb", "cc", "dd"],
    ["xx", "yy", "zz", "aa"]
]
mlist = ["aa", "bb", "cc", "dd"]

assert buddyListMax(mlist, blists) == 2
# assert buddyListMaxK(mlist, blists, 3) == [(2, 0), (3, 1), (4, 2)]
# assert buddyListRec(mlist, blists, 2) == set(['gg', 'ee'])
# assert buddyListRec(mlist, blists, 10) == set(['yy', 'zz', 'ee', 'gg', 'xx', 'ff'])

def recommend(mylist, blists, k):
    b_score = []
    for index in range(len(blists)):
        score = 0
        i = 0
        while i < len(blists[index]):
            if blists[index][i] in mylist:
                score += 1
                del(blists[index][i])
            else:
                i += 1
        b_score.append((index, score))

    b_score.sort(key=lambda x:x[1], reverse=True)

    rcmd_list = set()
    for t in b_score:
        if len(blists[t[0]]):
            for i in blists[t[0]]:
                rcmd_list.add(i)
                if len(rcmd_list) == k:
                    return rcmd_list
    return rcmd_list


# print recommend(mlist, blists, 10)
# print buddyListRec(mlist, blists, 10)
