def roundNum(nums=[]):

    total_real = round(sum(nums))
    out_list = []
    small_list = {}
    for i in range(len(nums)):
        round_ = round(nums[i])
        out_list.append(int(round_))
        if round_ <= nums[i]:
             #print nums[i], round_, nums[i]-round_
             if nums[i]-round_ not in small_list:
                 small_list[nums[i]-round_] = [i]
             else:
                 small_list[nums[i]-round_].append(i)
    diff = int(total_real- sum(out_list))
    sorted_key = sorted(small_list.keys())
    key = 0
    while diff > 0:
        if not key:
            big = sorted_key.pop()
            key = small_list[big]
        print big, key
        out_list[key[0]] += 1
        del(key[0])
        diff -= 1
    return out_list
# print roundNum([1.4, 0.2, 5.6, 1.4, 1.4])
# print '----------'

import math
def roundNum2(input):
    print input
    output = map(lambda x: math.floor(x), input)
    print output
    remain = int(round(sum(input)) - sum(output))
    print remain
    it = sorted(enumerate(input), key=lambda x: x[1] - math.floor(x[1]))
    #print 'it', it
    for _ in xrange(remain):
        output[it.pop()[0]] += 1
    #print sum(output), int(round(sum(input)))
    return output


print roundNum2([1.4, 0.2, 5.6, 1.4, 1.4])

from math import floor, ceil

def roundsum(clist):
  flist = [floor(c) for c in clist]
  diff = round(sum(clist))-sum(flist)

  dlist = [c-floor(c) for c in clist]
  ret = 0
  print dlist
  dlist.sort(reverse=True)
  for c in dlist:
    if diff>0:
      diff-=1
      ret+=1-c
    else:
      ret+=c

  print ret
  return ret

approx_equal = lambda a, b, t: abs(a - b) < t



#roundsum([1.2, 2.3, 3.4])
# assert approx_equal(roundsum([1.2, 2.3, 3.4]), 1.1, 0.0001)==True
# assert approx_equal(roundsum([1.2, 2.5, 3.6, 4.0]), 1.1, 0.0001)==True
# assert approx_equal(roundsum([1.2, 3.7, 2.3, 4.8]), 1.0, 0.0001)==True