'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        result = []
        for i in range(len(intervals)):
            intv = intervals[i]
            if intv[1] < newInterval[0] or intv[0] > newInterval[1]:
                result.append(intv)
                if i < len(intervals)-1 and intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[1]:
                    result.append(newInterval)
                    result  += intervals[i+1:]
                    break
            else:
                newInterval[0] = min(intv[0], newInterval[0])
                newInterval[1] = max(intv[1], newInterval[1])
                if result and not (result[-1][1] < newInterval[0] or result[-1][0] > newInterval[1]):
                    result[-1][0] = min(result[-1][0], newInterval[0])
                    result[-1][1] = max(result[-1][1], newInterval[1])
                else:
                    result.append(newInterval)
            #print result
        return result

    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right


obj = Solution()

intervals = [[3,5],[12,15]]


new = [6,6]
print obj.insert(intervals, new)







# [[1,3],[6,9]]
# [2,5]