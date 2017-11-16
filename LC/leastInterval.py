'''
Given a char array representing tasks CPU need to do. 
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. Each task could be done in one interval. 
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.
Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if len(tasks) == 0:
            return 0
        hash_set = {}
        total = 0
        max_n = 0
        for num in tasks:
            hash_set[num] = hash_set.get(num, 0) + 1
            max_n = max(hash_set[num], max_n)
        left = len(tasks) - (max_n-1)*(n+1)

        # print left, len(tasks), (max_n-1)*n
        # #sorted_list = sorted(hash_set.items(), key=lambda x:x[1])
        # print
        # #left = len(tasks) - sorted_list

        return total

    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        print cnt
        tmax = max(cnt.values())
        slots = (tmax - 1) * n
        print slots
        tsum = len(tasks)
        print tsum
        test = [n - (n == tmax) for n in cnt.values()]
        print test
        return tsum + max(0, slots + tmax - 1 - sum(n - (n == tmax) for n in cnt.values()))

s = Solution()
print s.leastInterval(['F','J','J','A','J','F','C','H','J','B','E','G','G','F','A','C','I','F','J','C','J','C','H','C','A','D','G','H','B','F','G','C','C','A','E','B','H','J','E','I','F','D','E','A','C','D','B','D','J','J','C','F','D','D','J','H','A','E','C','D','J','D','G','G','B','C','E','G','H','I','D','H','F','E','I','B','D','E','I','E','C','J','G','I','D','E','D','J','C','A','C','C','D','I','J','B','D','H','H','J','G','B','G','A','H','E','H','E','D','E','J','E','J','C','F','C','J','G','B','C','I','I','H','F','A','D','G','F','C','C','F','G','C','J','B','B','I','C','J','J','E','G','H','C','I','G','J','I','G','G','J','G','G','E','G','B','I','J','B','H','D','H','G','F','C','H','C','D','A','G','B','H','H','B','J','C','A','F','J','G','F','E','B','F','E','B','B','A','E','F','E','H','I','I','C','G','J','D','H','E','F','G','G','D','E','B','F','J','J','J','D','H','E','B','D','J','I','F','C','I','E','H','F','E','G','D','E','C','F','E','D','E','A','I','E','A','D','H','G','C','I','E','G','A','H','I','G','G','A','G','F','H','J','D','F','A','G','H','B','J','A','H','B','H','C','G','F','A','C','C','B','I','G','G','B','C','J','J','I','E','G','D','I','J','I','C','G','A','J','G','F','J','F','C','F','G','J','I','E','B','G','F','A','D','A','I','A','E','H','F','D','D','C','B','J','I','J','H','I','C','D','A','G','F','I','B','E','D','C','J','G','I','H','E','C','E','I','I','B','B','H','J','C','F','I','D','B','F','H','F','A','C','A','A','B','D','C','A','G','B','G','F','E','G','A','A','A','C','J','H','H','G','C','C','B','C','E','B','E','F','I','E','E','D','I','H','G','F','A','H','B','J','B','G','H','C','C','B','G','C','B','A','E','G','A','J','G','D','C','I','G','F','G','G','A','J','E','I','D','E','A','F','A','H','C','E','D','D','D','H','I','F','F','A','F','A','A','C','J','D','J','H','I','F','A','C','B','C','A','C','C','H','A','J','I','B','A','I','F','J','C','I','B','C','E','E','E','J','G','F','E','I','A','A','E','B','J','H','H','H','A','H','J','E','F','E','F','G','J','D','I','D','I','F','B','J','D','A','A','D','F','G','B','J','H','F','A','D','H','C','B','A','J','H','I','F','H','E','G','B','A','F','F','A','C','D','G','I','I','J','H','H','C','J','G','B','A','D','B','F','J','D','I','A','F','F','F','F','A','E','B','C','G','H','E','B','B','A','G','D','C','C','E','A','C','F','G','A','I','F','B','H','J','G','C','B','H','D','A','H','B','H','H','C','A','F','I','C','F','A','C','J','I','H','H','F','B','B','D','E','C','J','F','C','E','A','J','E','C','A','E','B','A','J','F','J','J','J','H','H','C','I','E','G','G','H','J','J','H','H','H','J','H','A','G','I','C','E','C','D','G','G','F','H','D','G','H','A','E','I','D','A','H','G','E','A','B','F','I','C','A','F','B','A','I','F','G','I','F','D','A','B','J','B','D','F','G','J','J','A','A','C','H','G','F','B','I','I','J','A','H','D','F','E','F','J','B','F','C','G','E','A','G','H','E','H','H','F','I','G','C','C','G','J','B','H','F','H','D','I','B','D','I','F','H','I','D','F','G','G','E','A','C','A','G','H','G','H','J','F','D','F','G','D','D','C','J','C','J','G','G','G','G','H','H','G','D','E','H','G','C','B','F','I','F','C','H','J','I','A','F','D','C','F','C','E','E','D','D','C','G','B','F','E','J','C','I','E','D','B','B','I','I','I','H','C','E','C','J','F','G','A','I','J','D','I','C','G','F','I','E','I','E','F','A','G','E','J','A','I','A','D','A','G','J','F','E','D','I','A','E','J','I','C','J','B','F','B','E','C','E','F','G','E','J','J','I','E','D','F','C','H','H','B','G','D','I','I','F','B','G','C','F','J','B','G','J','H','D','G','C','C','I','I','E','I','B','H','B','I','G','F','H','G','C','J','D','C','E','G','F','C','H','D','A','C','D','H','B','C','H','I','B','A','J','C','B','D','J','D','H','F','B','A','G','G','J','I','E','F','A','D','H','D','B','C','A','H','F','G','B','F','H','B','H','I','J','D','H','I','B','C','D','G','A','E','A','A','I','F','I','F','B','B','I','F','A','E','I','A','B','G','C','F','I','A','F','I','D','H','B','I','I','B','J','F','E','B','B','B','D','C','J','E','J','J','G','D','F','F','F','G','I','H','J','J','G','D','G','F'],8)

#print s.leastInterval2(['F','J','J','A','J','F','C','H','J','B','E','G','G','F','A','C','I','F','J','C','J','C','H','C','A','D','G','H','B','F','G','C','C','A','E','B','H','J','E','I','F','D','E','A','C','D','B','D','J','J','C','F','D','D','J','H','A','E','C','D','J','D','G','G','B','C','E','G','H','I','D','H','F','E','I','B','D','E','I','E','C','J','G','I','D','E','D','J','C','A','C','C','D','I','J','B','D','H','H','J','G','B','G','A','H','E','H','E','D','E','J','E','J','C','F','C','J','G','B','C','I','I','H','F','A','D','G','F','C','C','F','G','C','J','B','B','I','C','J','J','E','G','H','C','I','G','J','I','G','G','J','G','G','E','G','B','I','J','B','H','D','H','G','F','C','H','C','D','A','G','B','H','H','B','J','C','A','F','J','G','F','E','B','F','E','B','B','A','E','F','E','H','I','I','C','G','J','D','H','E','F','G','G','D','E','B','F','J','J','J','D','H','E','B','D','J','I','F','C','I','E','H','F','E','G','D','E','C','F','E','D','E','A','I','E','A','D','H','G','C','I','E','G','A','H','I','G','G','A','G','F','H','J','D','F','A','G','H','B','J','A','H','B','H','C','G','F','A','C','C','B','I','G','G','B','C','J','J','I','E','G','D','I','J','I','C','G','A','J','G','F','J','F','C','F','G','J','I','E','B','G','F','A','D','A','I','A','E','H','F','D','D','C','B','J','I','J','H','I','C','D','A','G','F','I','B','E','D','C','J','G','I','H','E','C','E','I','I','B','B','H','J','C','F','I','D','B','F','H','F','A','C','A','A','B','D','C','A','G','B','G','F','E','G','A','A','A','C','J','H','H','G','C','C','B','C','E','B','E','F','I','E','E','D','I','H','G','F','A','H','B','J','B','G','H','C','C','B','G','C','B','A','E','G','A','J','G','D','C','I','G','F','G','G','A','J','E','I','D','E','A','F','A','H','C','E','D','D','D','H','I','F','F','A','F','A','A','C','J','D','J','H','I','F','A','C','B','C','A','C','C','H','A','J','I','B','A','I','F','J','C','I','B','C','E','E','E','J','G','F','E','I','A','A','E','B','J','H','H','H','A','H','J','E','F','E','F','G','J','D','I','D','I','F','B','J','D','A','A','D','F','G','B','J','H','F','A','D','H','C','B','A','J','H','I','F','H','E','G','B','A','F','F','A','C','D','G','I','I','J','H','H','C','J','G','B','A','D','B','F','J','D','I','A','F','F','F','F','A','E','B','C','G','H','E','B','B','A','G','D','C','C','E','A','C','F','G','A','I','F','B','H','J','G','C','B','H','D','A','H','B','H','H','C','A','F','I','C','F','A','C','J','I','H','H','F','B','B','D','E','C','J','F','C','E','A','J','E','C','A','E','B','A','J','F','J','J','J','H','H','C','I','E','G','G','H','J','J','H','H','H','J','H','A','G','I','C','E','C','D','G','G','F','H','D','G','H','A','E','I','D','A','H','G','E','A','B','F','I','C','A','F','B','A','I','F','G','I','F','D','A','B','J','B','D','F','G','J','J','A','A','C','H','G','F','B','I','I','J','A','H','D','F','E','F','J','B','F','C','G','E','A','G','H','E','H','H','F','I','G','C','C','G','J','B','H','F','H','D','I','B','D','I','F','H','I','D','F','G','G','E','A','C','A','G','H','G','H','J','F','D','F','G','D','D','C','J','C','J','G','G','G','G','H','H','G','D','E','H','G','C','B','F','I','F','C','H','J','I','A','F','D','C','F','C','E','E','D','D','C','G','B','F','E','J','C','I','E','D','B','B','I','I','I','H','C','E','C','J','F','G','A','I','J','D','I','C','G','F','I','E','I','E','F','A','G','E','J','A','I','A','D','A','G','J','F','E','D','I','A','E','J','I','C','J','B','F','B','E','C','E','F','G','E','J','J','I','E','D','F','C','H','H','B','G','D','I','I','F','B','G','C','F','J','B','G','J','H','D','G','C','C','I','I','E','I','B','H','B','I','G','F','H','G','C','J','D','C','E','G','F','C','H','D','A','C','D','H','B','C','H','I','B','A','J','C','B','D','J','D','H','F','B','A','G','G','J','I','E','F','A','D','H','D','B','C','A','H','F','G','B','F','H','B','H','I','J','D','H','I','B','C','D','G','A','E','A','A','I','F','I','F','B','B','I','F','A','E','I','A','B','G','C','F','I','A','F','I','D','H','B','I','I','B','J','F','E','B','B','B','D','C','J','E','J','J','G','D','F','F','F','G','I','H','J','J','G','D','G','F'],8)
#print s.leastInterval(['A','A','A','B','B','B'],2)
#list = ['B','A', 'A','C', 'A', 'A', 'D', 'D', 'D', 'D', 'D', 'D', 'B']
#n = 3
#print s.leastInterval(list[:], n)
#print s.leastInterval2(list[:], n)