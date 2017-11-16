class Queue:
    def __init__(self):
        self.top = []
        self.tail = self.top
        self.head = -1

    def push(self, elem):
        if self.head == -1:
            self.head = 0

        if len(self.tail) == 1:
            self.tail.append([])
            self.tail = self.tail[-1]

        self.tail.append(elem)

    def pop(self):
        if self.head == -1:
            return None

        ret = self.top[self.head]
        self.head += 1
        if self.head == len(self.top):
            self.top = []
            self.head = -1
        else:
            if isinstance(self.top[self.head], list):
                self.top = self.top[self.head]
                self.head = 0

        return ret


q = Queue()
q.push(2)
q.push(3)
q.push(4)
q.push(5)

#assert q.top == [2, [3, [4]]]
# print q.top
# print q.pop()
# print q.pop()
# print q.pop()
# print q.pop()
# print q.pop()
# assert q.top == []


class Queue2(object):
    def __init__(self):
        self.queue = []
        self.count = 0
        #self.head = self.queue
        self.cur = self.queue

    def push(self, val):

        if self.count < 9:
            self.cur.append(val)
            self.count += 1
        else:
            self.cur.append([])
            self.cur = self.cur[9]
            self.cur.append(val)
            self.count = 1
        #self.cur = self.cur[10]
        #print self.cur
        #self.queue = self.queue[10]

    def pop(self):
        if len(self.queue) == 0:
            return False
        ret = self.queue[0]
        del(self.queue[0])
        if len(self.queue) and isinstance(self.queue[0], list):
            self.queue = self.queue[0]
        return ret


queue = Queue2()

for i in range(20):
    queue.push(i)
print queue.queue

for i in range(50):
    queue.pop()
