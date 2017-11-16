def decode(testEncStr):
    truth = "abc"
    if testEncStr == truth:
        return 123456
    return None


def decodeFind(badEncStr):
    n = len(badEncStr)
    q = [""]
    while q:
        cur = q.pop()
        idx = len(cur)
        #print cur
        if idx == n:
            print q
            break
            id = decode(cur)
            if id is not None:
                return id
            continue

        if badEncStr[idx].isalpha():
            #print 'is al'
            q.append(cur + badEncStr[idx].swapcase())

        q.append(cur + badEncStr[idx])

    return None


#

#print decodeFind("kLjjJ324hijKs_")


def decodeStr(badStr):
    n = len(badStr)
    all_list = [""]

    queue = [""]

    while queue:
        q = queue.pop()
        cur_length = len(q)
        if cur_length == n:
            if decode(q):
                return True
        else:
            if badStr[cur_length].isalpha():
                queue.append(q+badStr[cur_length].swapcase())
            queue.append(q+badStr[cur_length])
        print len(queue)
    return False



    # for i in badStr:
    #     temp_str = []
    #     for base in all_list:
    #         temp_str.append(base+ i)
    #         temp_str.append(base+ i.swapcase())
    #     all_list = temp_str
    # print all_list


print decodeStr("aBcddd")
# a = ''
# a.swapcase()

# assert decodeFind("kljJJ324hijks_") == 123456
# assert decodeFind("a") == None
# assert decodeFind("kljJJ324hijkS_") == 123456
# assert decodeFind("") == None

