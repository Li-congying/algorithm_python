'''
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people 
in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        n = len(people)
        if n in [0, 1]:
            return people
        
        people.sort(key=lambda x: - x[0]*n + x[1])
        
        ret = []
        for i in xrange(n):
            ret.insert(people[i][1], people[i])
        
        return ret
        '''

        new_queue = sorted(people, key=lambda x:(x[0], -x[1]), reverse=True)
        result = []
        for i in range(len(new_queue)):
            index = new_queue[i][1]
            result.insert(index, new_queue[i])
            #result = result[:index] + [new_queue[i]] + result[index:]

        return result

obj = Solution()
p = [[7,0], [4,4], [7,1], [6,1], [5,2], [5,0]]
print obj.reconstructQueue(p)
