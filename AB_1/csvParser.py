s = 'John,Smith,john.smith@gmail.com,"Los Angeles,1"'
def csvParser(s):
    result = []
    inQuote = False
    temp_str = ""
    i = 0
    while i < len(s):
        if inQuote:
            if s[i] == '"':
                if i == len(s) - 1:
                    result.append(temp_str)
                    temp_str = ""
                else:
                    if s[i+1] == '"':
                        temp_str += '"'
                        i += 1
                    else:
                        inQuote = False
            else:
                temp_str += s[i]
        else:
            if s[i] == '"':
                inQuote = True
            elif s[i] == ',':
                result.append(temp_str)
                temp_str = ""
            else:
                temp_str += s[i]

        i += 1

    if temp_str:
        result.append(temp_str)

    return '|'.join(result)

s1 =  csvParser(s)

print  s1










