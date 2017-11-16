'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z 
where different letters represent different tasks.Tasks could be done without original order. 
Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = {}
        for i in tasks:
            task_count[i] = task_count.get(i, 0) + 1

        task_count = sorted(task_count.items(), key=lambda x:x[1], reverse=True)
        base = 1
        for i in range(1, len(task_count)):
            print task_count[i]
            if task_count[i][1] == task_count[i-1][1]:
                base += 1
            else:
                break
        cur = (task_count[0][1]-1) * (n + 1) + base
        print task_count[0][1], base
        return max(len(tasks), cur)


obj = Solution()
print obj.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)