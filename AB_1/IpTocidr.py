import math

def ipTolong(ip):
    res = 0
    segs = ip.split('.')
    for seg in segs:
        res = res * 256 + int(seg)
    return res


def longToIp(ip):
    res = []
    while ip > 0:
        res.append(str(ip % 256))
        ip /= 256

    while len(res) != 4:
        res.append("0")
    return '.'.join(res[::-1])


def cidr(start, end):
    res = []
    while start <= end:
        lastOne = start & -start
        # print lastOne
        if lastOne == 0:
            maxMask = 0
        else:
            maxMask = 32 - int(math.log(lastOne, 2))
        leftlen = 32 - int(math.log(end - start + 1, 2))
        mask = max(maxMask, leftlen)  # larger mask == smaller range cover
        # print maxMask,end,bin(start),mask
        res.append("{}/{}".format(longToIp(start), mask))
        start += 2 ** (32 - mask)
    return res


def cidr_range(start_ip, end_ip):
    start = ipTolong(start_ip)
    end = ipTolong(end_ip)
    return cidr(start, end)


def cidr_len(start_ip, num):
    start = ipTolong(start_ip)
    end = start + num - 1
    return cidr(start, end)


# assert cidr_range("5.10.64.1", "5.10.127.255") == ['5.10.64.1/32', '5.10.64.2/31', '5.10.64.4/30', '5.10.64.8/29',
#                                                    '5.10.64.16/28', '5.10.64.32/27', '5.10.64.64/26', '5.10.64.128/25',
#                                                    '5.10.65.0/24', '5.10.66.0/23', '5.10.68.0/22', '5.10.72.0/21',
#                                                    '5.10.80.0/20', '5.10.96.0/19']
# assert cidr_len("7.7.7.7", 5) == ['7.7.7.7/32', '7.7.7.8/30']
# assert cidr_len("0.0.0.0", 5) == ['0.0.0.0/30', '0.0.0.4/32']
# assert cidr_len("255.255.255.255", 1) == ['255.255.255.255/32']
# assert cidr_range("1.1.1.111", "1.1.1.120") == ['1.1.1.111/32', '1.1.1.112/29', '1.1.1.120/32']
# assert cidr_range("0.0.0.0", "255.255.255.255") == ['0.0.0.0/0']

def ipToLong(ip_str):
    list_ = ip_str.split(".")
    long = 0
    for i in range(len(list_)):
        long += int(list_[len(list_)-1-i]) * 256**i
    return long

def longToIp(long):
    list_ = []
    i = 3
    while i >= 0:
        list_.append(str(long/256**i))
        long = long%256**i
        i = i-1

    return ".".join(list_)


def cidrRang(start, end):
    range_list = []
    while start <= end:
        if start %2 == 1:
            range_list.append((start, 32))
            start += 1
        else:
            i = 1
            base = 0xFFFFFFFF

            while start & (base<<i) >= start and start + 2**i -1 <= end:
                i += 1
            range_list.append((start, 32-i+1))
            start = start + 2**(i-1)
            #print start

    result = []
    for item in range_list:
        str_ = longToIp(item[0])+"/"+str(item[1])
        result.append(str_)
    print result



# start =  ipToLong('0.0.0.1')
# end = ipToLong('0.0.0.8')

# print start, end
#cidrRang(start, end)
#
# res = cidr(start, end)
# print res


def ipToNum(ip):
    lt = ip.split('.')
    num = 0
    for i in range(len(lt)):
        num += int(lt[i]) * 256 ** (3 - i)
    return num


def numToIp(num):
    lt = []
    for i in range(4)[::-1]:
        lt.append(str(num / 256 ** i))
        num = num % 256 ** i
    ip = ".".join(lt)
    return ip


# num = ipToNum(ip2)
# print numToIp(num)

def groupIp(ip1, ip2):
    num1 = ipToNum(ip1)
    num2 = ipToNum(ip2)
    result = []
    while num1 <= num2:

        share = 0
        base1 = 0xFFFFFFFF
        base2 = 0
        print base1, base2, num1, num2
        while num1 & base1 >= num1 and num1 | base2 <= num2:
            base1 = base1 << 1
            base2 = (base2 << 1) + 1
            share += 1

        result.append((numToIp(num1), 32 - share + 1))
        num1 = (num1 | base2) + 1

    print result

start = '1.0.0.1'
end = '1.0.0.8'

groupIp(start, end)



