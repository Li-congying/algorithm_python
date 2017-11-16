class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        print s
        rep_time = ""
        result = ""
        other = ""
        left =  []
        for i in range(len(s)):
            if s[i] == '[':
                left.append(i)
                continue
            if s[i] == ']':
                start = left.pop()
                if not left:
                    if not rep_time:
                        rep_time = '1'
                    if other:
                        result += other
                        other = ""
                    result += int(rep_time) * self.decodeString(s[start+1:i])
                    rep_time = ""
                continue
            if not left:
                if s[i].isdigit():
                    rep_time += s[i]
                else:
                    other += s[i]
        if other:
            result += other
        return result

s = "3[a]2[bc]"

solu = Solution()
print solu.decodeString(s)