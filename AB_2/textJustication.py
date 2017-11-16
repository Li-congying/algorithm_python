words = ["This", "is", "an", "example", "of", "text", "justifi", "ca"]
maxWidth = 12


def textJustification(words, maxWidth):
    cur_length = 0
    result = []
    temp = []
    i = 0
    while i < len(words):

        if cur_length + len(temp) + len(words[i]) <= maxWidth:
            cur_length += len(words[i])
            temp.append(words[i])
            i += 1
        else:
            temp_str = ""
            if len(temp) == 1:
                temp_str = temp[0] + " " * (maxWidth - cur_length)
            else:
                base = (maxWidth - cur_length) / (len(temp) - 1)
                extra = (maxWidth - cur_length) % (len(temp) - 1)
                for j in range(len(temp)):
                    if j != len(temp) - 1:
                        if j < extra:
                            temp_str += temp[j] + " " * base + " "
                        else:
                            temp_str += temp[j] + " " * base
                    else:
                        temp_str += temp[j]
            result.append(temp_str)
            temp = []
            cur_length = 0
            # print i

    if temp:
        str_ = " ".join(temp)
        str_ += (maxWidth - len(str_)) * " "
        result.append(str_)

    for _str in result:
        print len(_str), _str


textJustification(words, maxWidth)