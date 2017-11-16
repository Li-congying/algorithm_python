# ABC
g = {'A': {'A': 'B', 'B': 'AC', 'C': 'A'},
     'B': {'A': 'C', 'B': 'A', 'C': 'C'},
     'C': {'A': 'B', 'B': 'C', 'C': 'A'}}


def isPath(src, target):
    ns, nt = len(src), len(target)
    last = set([src])
    for i in range(nt, ns):
        next = []
        print 'last', last
        for s in last:
            solutions = []
            ret = []
            print 's', s
            helper(s, 1, ret, solutions)
            next += solutions

        print 'next', next
        last = set(next)
        if target in last:
            return True
    return False


def helper(s, start, ret, solutions):
    if start >= len(s):
        solutions.append(''.join(ret))
        return

    cur = s[start - 1:start + 1]
    for nxt in g[cur[0]][cur[1]]:
        print 'nxt', nxt
        helper(s, start + 1, ret + [nxt], solutions)


# print isPath("ABCC", "A")
# print isPath("AC", "B")


def checkRoot(g, base, target):
    print base
    if len(base) == 1 :
        if base == target:
            return True
        else:
            return False
    if len(base) > 1:
        last_level = []
        for i in range(len(base)-1):
            #print base[i], base[i+1],
            temp_list = []
            #print g[base[i]][base[i+1]]
            for root_ in g[base[i]][base[i+1]]:
                if len(last_level) == 0:
                    temp_list.append(root_)
                else:
                    for i in last_level:
                        temp_list.append(i+root_)
            last_level = temp_list
            print last_level
        for nxt in last_level:
            if checkRoot(g, nxt, target):
                return True
        else:
            return False


#print checkRoot(g, "ACBB", "C")
#print isPath("ACBB", "C")

a = "/a/b/c"
b = ["zijzllb","r"]
c = sorted(b)
print b, c