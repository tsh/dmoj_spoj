import sys
sys.setrecursionlimit(15000)


class UnionFind:
    def __init__(self, L):
        self.parent = [i for i in range(L+1)]

    def find(self, el):
        if self.parent[el] == el:
            return el
        self.parent[el] =self.find(self.parent[el])
        return self.parent[el]


    def union(self, el, rep):
        set1 = self.find(el)
        set2 = self.find(rep)
        self.parent[set1] = set2
        if set1 == set2:
            self.parent[set2] = 0
        print('LADICA')


inp = sys.stdin.readline().split()
N,L = int(inp[0]), int(inp[1])
uf = UnionFind(L)
for _ in range(N):
    inp = sys.stdin.readline().split()
    a,b = int(inp[0]), int(inp[1])

    if uf.find(a) == a:
        uf.union(a,b)
    elif uf.find(b) == b:
        uf.union(b,a)
    elif uf.find(a) > 0:
        uf.union(a,b)
    elif uf.find(b) > 0:
        uf.union(b,a)
    else:
        print('SMECE')

