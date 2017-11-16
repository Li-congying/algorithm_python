class iter2D(object):
    def __init__(self, vec):
        self.vec = vec
        self.row = 0
        self.col = 0
        self.last_row = 0
        self.last_col = 0

    def next(self):
        if not self.has_next():
            return False
        self.last_row = self.row
        self.last_col = self.col

        val = self.vec[self.row][self.col]
        self.col += 1
        return val

    def has_next(self):

        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0
        return self.row < len(self.vec)

    def remove(self):
        del (self.vec[self.last_row][self.last_col])
        # self.last_row =
        self.last_row = self.row
        self.last_col = self.col


vec = [[], [1, 2, 3], [1], [4, 5]]

iter = iter2D(vec)
while iter.has_next():
    val = iter.next()
    print val
    if val == 1 or val == 3:
        iter.remove()

print vec



