'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        total = 0
        cur_char = ''
        cur_count = 0
        chars.append('')
        for char in chars:
            if cur_char != char:
                # print cur_char, cur_count
                chars[total] = cur_char
                if cur_count == 1:
                    total += 1
                if cur_count > 1:
                    str_c = str(cur_count)
                    for i in range(len(str_c)):
                        chars[total+1+i] = str_c[i]
                    total += (1+len(str(cur_count)))

                cur_char = char
                cur_count = 0
            cur_count += 1

        print chars[:total]
        return total

obj = Solution()
print obj.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])