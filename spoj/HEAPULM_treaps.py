import sys

class SegTreeNode:
    def __init__(self, left=None, right=None, max_index=None):
        self.left = left
        self.right = right
        self.max_index = max_index

    def __repr__(self):
        return f'<{self.left}/{self.max_index}\{self.right}>'

class SegmentTree:
    def __init__(self, treaps: list):
        n = len(treaps) - 1
        self.segtree = [None] * (n*4+1)
        self.treaps = treaps
        self.__init_segtree(1, 0, n)
        self.__fill_segtree(1)

    def __init_segtree(self, i, left, right):
        self.segtree[i] = SegTreeNode(left, right)
        if left == right:
            return
        mid = (left+right) //2
        self.__init_segtree(i*2, left, mid)
        self.__init_segtree(i*2+1, mid+1, right)

    def __fill_segtree(self, i):
        if self.segtree[i].left == self.segtree[i].right:
            self.segtree[i].max_index = self.segtree[i].left
            return self.segtree[i].max_index

        max_left_idx = self.__fill_segtree(i*2)
        max_right_idx = self.__fill_segtree(i*2+1)

        if self.treaps[max_left_idx].priority > self.treaps[max_right_idx].priority:
            max_idx = max_left_idx
        else:
            max_idx = max_right_idx
        self.segtree[i].max_index = max_idx
        return max_idx

    def query(self, i, left, right):
        # node segment has no in common with query
        if right < self.segtree[i].left or left > self.segtree[i].right:
            return float('-inf')
        # node segment is fully contained in query
        if left <= self.segtree[i].left and self.segtree[i].right <= right:
            return self.segtree[i].max_index
        # node segment contains part of query
        max_left_idx = self.query(i*2, left, right)
        max_right_idx = self.query(i*2+1, left, right)
        if max_left_idx == float('-inf'):
            return max_right_idx
        if max_right_idx == float('-inf'):
            return max_left_idx
        if self.treaps[max_left_idx].priority > self.treaps[max_right_idx].priority:
            return max_left_idx
        return max_right_idx


    def __repr__(self):
        return str(self.segtree)


class Node:
    def __init__(self, label=None, priority=None):
        self.label = label
        self.priority = priority

    def __repr__(self):
        return f'<{self.label}:{self.priority}>'

def max_priority_index(arr):
    maxi = i = 0
    while i < len(arr):
        if arr[i].priority > arr[maxi].priority:
            maxi = i
        i += 1
    return maxi

def solve(treaps, segtree, left, right):
    if left > right:
        return
    root_idx = segtree.query(1, left, right)
    root = treaps[root_idx]
    print('(', end='')
    solve(treaps, segtree, left, root_idx-1)
    print(f'{root.label}/{root.priority}', end='')
    solve(treaps, segtree, root_idx+1, right)
    print(')', end='')


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        inp = line.split()
        if inp[0] == '0':
            break
        treaps = []
        for el in inp[1:]:
            l, p = el.split('/')
            p = int(p)
            treaps.append(Node(label=l, priority=p))
        treaps.sort(key=lambda x: x.label)
        segtree = SegmentTree(treaps)
        solve(treaps, segtree, 0, len(treaps)-1)
        print('')
