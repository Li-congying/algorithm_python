'''
You are given a string, s, and a list of words, 
words, that are all of the same length. Find all starting indices of substring(s) 
in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        trie = {}
        for word in words:
            node = trie
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node['#'] = 1


        node = trie
        cur_word = ''
        start = 0
        start_pos = {}
        i = 0
        while i < len(s):
            if s[i] in node:
                cur_word += s[i]
                node = node[s[i]]
                if '#' in node:
                    start_pos[start] = cur_word
                    start = i+1
                    node = trie
                    cur_word = ''
            else:
                cur_word = ''
                if node != trie:
                    i -= 1
                    node = trie
                start = i + 1
            i += 1

        result = []
        print start_pos
        for pos, word in start_pos.items():
            check_table = {}
            next_pos = pos
            while next_pos in start_pos and start_pos[next_pos] not in check_table:
                check_table[start_pos[next_pos]] = 1
                next_pos += len(word)
            if len(check_table) == len(words):
                result.append(pos)

        return result

        #print check_table

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
obj = Solution()
print obj.findSubstring(s, words)