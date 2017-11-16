def is_palindrome(s):
    if len(s) <= 1:
        return True
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    else:
        return True

def palindrome_pair(string_list = []):

    string_index = {}
    for i in range(len(string_list)):
        string_index[string_list[i]] = i
    pairs = []
    for i in range(len(string_list)):
        string = string_list[i]
        for j in range(len(string)):
            if j == 0:
                reverse = string[::-1]
                # print reverse
                if reverse in string_index and string_index[reverse] != i:
                    pairs.append([i, string_index[reverse]])
                if is_palindrome(string):
                    if "" in string_list and string_index[""] != i:
                        pairs.append([i, string_index[""]])
                        pairs.append([string_index[""], i])
            else:
                if is_palindrome(string[:j]):
                    left_reverse = string[len(string):j-1:-1]
                    #print 'left', string[:j], left_reverse
                    if left_reverse in string_index and string_index[left_reverse] != i:
                        if [string_index[left_reverse], i] not in pairs:
                            pairs.append([string_index[left_reverse], i])
                if is_palindrome(string[len(string)-j:]) :
                    right_reverse = string[len(string)-1-j::-1]
                    #print 'right', string[j:], right_reverse
                    if right_reverse in string_index and string_index[right_reverse] != i:
                        if [i,string_index[right_reverse]] not in pairs:
                            pairs.append([i, string_index[right_reverse]])
            #print i, string, pairs, j

    return pairs


#print palindrome_pair(["a","abc","aba",""])


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        d = {w[::-1]: i for i, w in enumerate(words)}
        print d
        for i in range(len(words)):
            w = words[i]
            for j in range(len(w)+1):
                prefix, suffix = w[:j], w[j:]
                #print w, prefix
                if prefix in d and i != d[prefix] and suffix == suffix[::-1]:
                    print w, prefix
                    res.append([i, d[prefix]])
                if j > 0 and suffix in d and i != d[suffix] and prefix == prefix[::-1]:
                    res.append([d[suffix], i])
        return res

s = Solution()
print s.palindromePairs(["a","abc","aba","ba",""])