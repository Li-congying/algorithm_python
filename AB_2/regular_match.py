def regularMatch2(s, p):

    print s, p
    if p == '':
        return s == ''

    if len(p) >= 2 and p[1] == '*':

        if len(s) and (s[0] == p[0] or p[0] == '.'):
            if regularMatch2(s[1:], p):
                return True

        return regularMatch2(s, p[2:])

    elif len(s) and (s[0] == p[0] or p[0] == '.'):
        return regularMatch2(s[1:], p[1:])
    else:
        return False

print regularMatch2('aa', 'a')

set = set()
set.add((1,0))
print (0, 1) in set