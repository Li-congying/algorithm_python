words = ["This", "is", "an", "example", "of", "text", "justifi"]
maxWidth = 16


def text_justification(words, maxWidth):
    cur_length = 0
    i = 0
    temp = []
    result = []
    while i < len(words):
        if cur_length + len(temp) + len(words[i]) <= maxWidth:
            cur_length += len(words[i])
            temp.append(words[i])
            i += 1
        else:
            if len(temp) == 1:
                result.append(temp[0] + (maxWidth - cur_length) * " ")
            else:
                extra_space = maxWidth - cur_length
                base = extra_space / (len(temp) - 1)
                more = extra_space % (len(temp) - 1)
                str_ = ""
                for j in range(len(temp)):
                    str_ += temp[j]
                    if j < len(temp) - 1:
                        if j < more:
                            str_ += (base + 1) * " "
                        else:
                            str_ += base * " "
                result.append(str_)
            temp = []
            cur_length = 0

    if len(temp):
        str_ = " ".join(temp)
        str_ += (maxWidth - len(str_)) * " "
        result.append(str_)

    for i in result:
        print i, len(i)

    return result


text_justification(words, maxWidth)