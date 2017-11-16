'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def minifyHeap(self, index = 0):
        small = index
        if index*2+1 < len(self.min_heap) and self.min_heap[index*2+1] < self.min_heap[index]:
            small = index * 2 + 1

        if index*2+2 < len(self.min_heap) and self.min_heap[index*2+2] < self.min_heap[small]:
            small = index * 2 + 2
        if small != index:
            self.min_heap[index], self.min_heap[small] = self.min_heap[small], self.min_heap[index]
            self.minifyHeap(small)

    def maxifyHeap(self, index = 0):
        large = index
        if index * 2 + 1 < len(self.max_heap) and self.max_heap[index * 2 + 1] > self.max_heap[index]:
            large = index * 2 + 1
        if index * 2 + 2 < len(self.max_heap) and self.max_heap[index * 2 + 2] > self.max_heap[large]:
            large = index * 2 + 2
        if large != index:
            self.max_heap[index], self.max_heap[large] = self.max_heap[large], self.max_heap[index]
            self.maxifyHeap(large)

    def addToMinHeap(self, value):
        print 'add  min', value
        self.min_heap =  self.min_heap + [value]
        print self.min_heap
        #self.minifyHeap(0)
        index = len(self.min_heap) - 1
        print index, self.min_heap[(index - 1) / 2]
        while index > 0 and self.min_heap[(index - 1) / 2] > self.min_heap[index]:
            self.min_heap[index], self.min_heap[(index - 1) / 2] = self.min_heap[(index - 1) / 2], self.min_heap[index]
            index = (index - 1) / 2

    def addToMaxHeap(self, value):
        self.max_heap = self.max_heap + [value]
        index = len(self.max_heap)-1
        while index > 0 and self.max_heap[(index-1)/2] < self.max_heap[index]:
            self.max_heap[index], self.max_heap[(index-1)/2] =  self.max_heap[(index-1)/2] , self.max_heap[index]
            index = (index-1)/2

        #self.maxifyHeap(0)

    # def popHeap(self, heap):
    #     if not heap:
    #         return False
    #     val = heap.pop(0)
    #     return val
    def popMaxHeap(self):
        if not self.max_heap:
            return None
        self.max_heap[0], self.max_heap[-1] = self.max_heap[-1], self.max_heap[0]
        val = self.max_heap.pop()
        self.maxifyHeap(0)
        return val

    def popMinHeap(self):
        if not self.min_heap:
            return None
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        val = self.min_heap.pop()
        self.minifyHeap(0)
        return val

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.max_heap or num < self.max_heap[0]:
            self.addToMaxHeap(num)
        else:
            self.addToMinHeap(num)
        #print self.max_heap, self.min_heap,
        if len(self.max_heap) - len(self.min_heap) >= 2:
            val = self.popMaxHeap()
            self.addToMinHeap(val)

        elif len(self.min_heap) - len(self.max_heap) >= 2:
            val = self.popMinHeap()
            self.addToMaxHeap(val)

        if self.min_heap:
            print  min(self.min_heap), self.min_heap # self.min_heap

    def findMedian(self):
        """
        :rtype: float
        """
        if self.max_heap and len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + self.max_heap[0])/2.0
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return False



from heapq import *
class MedianFinder2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = [] # higher half
        self.max_heap = [] # lower half

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.max_heap or -self.max_heap[0] <= num:
            heappush(self.min_heap, num)
            if len(self.min_heap) - len(self.max_heap) > 1:
                heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.max_heap, -num)
            if len(self.max_heap) - len(self.min_heap) > 1:
                heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]


obj = MedianFinder()

# obj.min_heap = [5, 6, 8, 7]
# obj.addToMinHeap(9)
# print obj.min_heap
list = [18, 251, 158, 158, 529, 180, 134, 529, 240, 435, 435, 316, 350, 537, 490, 198, 359, 493, 585, 614, 21, 583, 106, 549, 271, 174, 430, 222, 117, 159, 206, 100, 496, 129, 550, 411, 216, 271, 98, 119, 232, 629, 101, 218, 53, 468, 447, 402, 603, 584, 306, 269, 623, 88, 79, 521, 261, 544, 628, 121, 278, 132, 105, 72, 459, 408, 111, 291, 437, 7, 276, 34, 16, 254, 177, 550, 632, 464, 191, 167, 158, 331, 187, 123, 274, 321, 182, 93, 277, 595, 459, 349, 80, 195, 195, 214, 14, 384, 68, 427, 84, 609, 283, 59, 234, 327, 330, 509, 568, 65, 442, 380, 321, 589, 603, 64, 486, 175, 204, 421, 381, 209, 578, 580, 294, 287, 518, 261, 619, 155, 636, 287, 250, 209, 586, 299, 589, 65, 34, 216, 507, 380, 127, 186, 135, 533, 272, 563, 249, 350, 516, 229, 307, 127, 306, 195, 537, 269, 485, 446, 206, 222, 515, 240, 266, 417, 472, 140, 185, 439, 592, 283, 273, 188, 230, 195, 217, 321, 246, 563, 113, 411, 290, 351, 221, 76, 399, 19, 142, 544, 47, 270, 614, 36, 538, 179, 370, 387, 513, 570, 546, 347, 181, 257, 182, 412, 588, 66, 276, 381, 94, 461, 570, 550, 432, 192, 153, 382, 568, 233, 375, 186, 469, 402, 266, 143, 146, 44, 512, 540, 297, 520, 545, 436, 412, 597, 535, 13, 12, 109, 128, 84, 619, 85, 203, 478, 367, 77, 485, 640, 415, 533, 628, 338, 542, 560, 11, 80, 277, 148, 113, 23, 246, 453, 221, 310, 486, 262, 87, 330, 390, 199, 451, 540, 283, 466, 37, 639, 515, 319, 520, 289, 620, 470, 216, 249, 229, 130, 134, 637, 350, 605, 481, 220, 373, 60, 100, 205, 270, 305, 166, 525, 373, 627, 607, 111, 91, 491, 143, 353, 549, 434, 182, 386, 33, 540, 364, 456, 635, 317, 637, 0]
for i in list:
    obj.addNum(i)
#     #print obj.findMedian()

#print obj.min_heap, obj.max_heap

# list = [350, 435, 359, 529, 537, 435, 490, 493, 585, 614, 583, 549, 529]
# for i in list:
#     obj.addToMinHeap(i)
# #obj.addToMinHeap(430)
# print obj.popMinHeap()
# print obj.popMinHeap()
# print obj.min_heap
