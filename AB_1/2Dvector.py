class TwoDIterator:
    def __init__(self, clist):
        self.clist = clist
        self.rowId = 0
        self.colId = 0
        self.flag = True

    def hasNext(self):
        """
        self.rowId, self.colId
        """
        nrow = len(self.clist)
        while self.rowId < nrow and self.colId == len(self.clist[self.rowId]):
            self.rowId += 1
            self.colId = 0
        return self.rowId < nrow

    def next(self):
        self.hasNext()
        ret = self.clist[self.rowId][self.colId]
        self.colId += 1
        self.flag = True
        return ret

    def remove(self):
        if not self.flag:
            return
        rowrm, colrm = self.rowId, self.colId
        print 'remove', rowrm,colrm
        # self.colId==0 can never happen
        colrm -= 1
        del self.clist[rowrm][colrm]

        if not self.clist[rowrm]:
            del self.clist[rowrm]
            # no need to adjust rowId, as I am still pointing to the old rowId
            self.colId = 0
        else:
            self.colId -= 1
        self.flag = False
        # print self.rowId,self.colId


clist = [[1, 2, 3,4],[], [4], [5]]
ti = TwoDIterator(clist)
while ti.hasNext():
    ret = ti.next()
    print ret,
    if ret == 4 :
        ti.remove()
        ti.remove()
print ti.clist

# assert clist == [[1, 2], [4]]


# assert clist==[[],[1,2],[3],[]]


class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.rowId = 0
        self.colunmId = 0
        self.last_rowId = 0
        self.last_colunmId = 0

    def next(self):
        """
        :rtype: int
        """
        #print self.colunmId, self.rowId, len(self.vec2d[0])
        self.last_rowId = self.rowId
        self.last_colunmId = self.colunmId
        print 'start', self.rowId, self.colunmId
        val = self.vec2d[self.rowId][self.colunmId]
        self.colunmId += 1
        print 'end',self.rowId, self.colunmId,
        return val


    def hasNext(self):
        """
        :rtype: bool
        """
        print 'has next', self.rowId, self.colunmId
        while self.rowId < len(self.vec2d) and self.colunmId == len(self.vec2d[self.rowId]):
            self.rowId += 1
            self.colunmId = 0

        if self.rowId >=len(self.vec2d):
            return False
        if self.colunmId >= len(self.vec2d[self.rowId]):
            return False
        return True

    def remove(self):
        if self.colunmId <= 0 and self.rowId <= 0:
            return False
        del(self.vec2d[self.last_rowId][self.last_colunmId])
        self.colunmId = self.last_colunmId
        self.rowId = self.last_rowId





# vec = Vector2D([[1, 2, 3,6], [4,4,6], [],[5,8,9], [4,6]])
# while vec.hasNext():
#     ret =  vec.next()
#     print 'ret', ret
#     if ret == 6 or ret == 1:
#         vec.remove()
# #
# print vec.vec2d