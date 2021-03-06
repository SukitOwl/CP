class QU():
    def __init__(self):
        self.id = [None] * n
        self.sz = [1] * n
        for i in self.id:
            self.id[i] = i

    def root(self, i: int):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p: int, q: int):
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        if (i == j):
            return 0
        if sz[i] < sz[j]:
            self.id[i] = j; self.sz[j] += self.sz[i]
        else:
            self.id[j] = i; self.sz[i] += self.sz[j]
