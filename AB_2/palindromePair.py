words = ["bb", "bababab", "baab", "abaabaa", "aaba", "", "bbaa", "aba", "baa", "b"]


def isPalindrome(word):
    for i in range(len(word) / 2):
        if word[i] != word[-(i + 1)]:
            return False
    else:
        return True


def palindromePair(words):
    word_map = {}
    for i in range(len(words)):
        word_map[words[i][::-1]] = i

    result = []
    for i in range(len(words)):
        word = words[i]
        if word == '':
            continue
        if isPalindrome(word):
            if '' in word_map:
                result.append([word_map[''], i])
                result.append([i, word_map['']])
        if word in word_map and word_map[word] != i:
            result.append([i, word_map[word]])

        for j in range(1, len(word)):
            if isPalindrome(word[j:]) and word[:j] in word_map:
                result.append([i, word_map[word[:j]]])
            if isPalindrome(word[:j]) and word[j:] in word_map:
                result.append([word_map[word[j:]], i])
                # print word, word[i:], word[:i]
                # break

    print result


palindromePair(words)
