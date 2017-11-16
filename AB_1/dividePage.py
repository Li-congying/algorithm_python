items = [
  "1,28,300.1,SanFrancisco",
  "4,5,209.1,SanFrancisco",
  "20,7,208.1,SanFrancisco",
  "23,8,207.1,SanFrancisco",
  "16,10,206.1,Oakland",
  "1,16,205.1,SanFrancisco",
  "6,29,204.1,SanFrancisco",
  "7,20,203.1,SanFrancisco",
  "8,21,202.1,SanFrancisco",
  "2,18,201.1,SanFrancisco",
  "2,30,200.1,SanFrancisco",
  "15,27,109.1,Oakland",
  "10,13,108.1,Oakland",
  "11,26,107.1,Oakland",
  "12,9,106.1,Oakland",
  "13,1,105.1,Oakland",
  "22,17,104.1,Oakland",
  "1,2,103.1,Oakland",
  "28,24,102.1,Oakland",
  "18,14,11.1,SanJose",
  "6,25,10.1,Oakland",
  "19,15,9.1,SanJose",
  "3,19,8.1,SanJose",
  "3,11,7.1,Oakland",
  "27,12,6.1,Oakland",
  "1,3,5.1,Oakland",
  "25,4,4.1,SanJose",
  "5,6,3.1,SanJose",
  "29,22,2.1,SanJose",
  "30,23,1.1,SanJose"
        ]

def divide_page(items, page_size):
    page_nums = len(items)/page_size if len(items)%page_size==0 else len(items)/page_size + 1
    page_list = [[] for i in range(page_nums)]
    page_index = 0

    while page_index < page_nums-1:
        hash_set = {}
        cur_size = 0
        i = 0
        while i < len(items):
            host_id = items[i].split(',')[0]
            if host_id not in hash_set:
                hash_set[host_id] = 1
                cur_size += 1
                page_list[page_index].append(items[i])
                del(items[i])
            else:
                i += 1
            if cur_size == page_size:
                page_index += 1
                break
            if i == len(items)-1 and cur_size < page_size:
                hash_set = {}
                i = 0
        if page_index == page_nums-1:
            page_list[page_index] = items
            break
    return page_list

def pagedisplay(input_csv_array, k):
    ids = [line.split(',')[0] for line in input_csv_array]
    hmap = {}
    pages = []
    start = 0

    for i, id in enumerate(ids):
        if id not in hmap or hmap[id] < start:
            hmap[id] = start
        print 'i', i, 'host_id', id, 'pos', hmap[id], len(pages)
        if hmap[id] == len(pages):
            pages.append([])
        pages[hmap[id]].append(input_csv_array[i])
        hmap[id] += 1
        if len(pages[start]) == k:
            start += 1

    # if you need to print exact k lines in a page (i.e., tolerate some dup)
    # then have a third loop to print the page
    for page in pages:
        print '---- page ----'
        for line in page:
            print line


def paginate(num, results):

    # if len(results) == 0:
    #     return ["\n"]
    page_nums = len(results)/num if len(results)%num==0 else len(results)/num + 1
    page_list = [[] for i in range(page_nums)]
    page_index = 0

    while page_index <= page_nums-1:
        hash_set = {}
        cur_size = 0
        i = 0
        while i < len(results):
            host_id = results[i].split(',')[0]
            if host_id not in hash_set:
                hash_set[host_id] = 1
                cur_size += 1
                page_list[page_index].append(results[i])
                del(results[i])
            else:
                i += 1
            if cur_size == num:
                page_index += 1
                break
            if i == len(results) and cur_size < num:
                page_list[page_index] += results[:num-cur_size]
                del(results[:num-cur_size])
                page_index += 1
                break

        if len(results) == 0:
            break

    result = []
    for page in page_list:
        str_ = '\n'.join(page)+'\n'
        result.append(str_)

    return result




list_ =["1,28,300.1,San Francisco",
"4,5,209.1,San Francisco",
"20,7,208.1,San Francisco",
"23,8,207.1,San Francisco",
"16,10,206.1,Oakland",
"1,16,205.1,San Francisco",
"1,31,204.6,San Francisco",
"6,29,204.1,San Francisco",
"7,20,203.1,San Francisco",
"8,21,202.1,San Francisco",
"2,18,201.1,San Francisco",
"2,30,200.1,San Francisco",
"15,27,109.1,Oakland",
"10,13,108.1,Oakland",
"11,26,107.1,Oakland",
"12,9,106.1,Oakland",
"13,1,105.1,Oakland",
"22,17,104.1,Oakland",
"1,2,103.1,Oakland",
"28,24,102.1,Oakland",
"18,14,11.1,San Jose",
"6,25,10.1,Oakland",
"19,15,9.1,San Jose",
"3,19,8.1,San Jose",
"3,11,7.1,Oakland",
"27,12,6.1,Oakland",
"1,3,5.1,Oakland",
"25,4,4.1,San Jose",
"5,6,3.1,San Jose",
"29,22,2.1,San Jose",
"30,23,1.1,San Jose"]



res =  paginate(4, [])
for res_cur in res:
    print str(res_cur) + "\n"

