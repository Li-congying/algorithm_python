def miniParser(s):
    s = s.strip()
    #print 's', s
    if len(s) == 0:
        return '';
    if s[0] != '[':
        return int(s)
    if len(s) == 2:
        return []
    result = []
    temp = ''
    left_count = 0
    for i in range(1,len(s)-1):
        if s[i] == '[':
            left_count += 1
        if s[i] == ']':
            left_count -= 1
        if left_count or s[i] != ',':
            temp += s[i]
        if not left_count and (s[i] == ',' or i == len(s)-2):
            result.append(miniParser(temp))
            temp = ''

    return result

#a =  miniParser("[[],[[[[]],-4],[[[]],[0],[[]]]]]")

#print a
#print a, isinstance(a, list)

import math
#print math.sqrt(13)

a = [['b'], ['a']]
print ','.join(a)