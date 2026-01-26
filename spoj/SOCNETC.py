import sys


def find(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, size, x, y, M):
    community1 = find(parent,  x)
    community2 = find(parent,  y)
    if community1 != community2 and (size[community1] + size[community2]) <= M:
        if size[community2] > size[community1]:
            size[community2] = size[community1] + size[community2]
            parent[community1] = community2
        else:
            size[community1] = size[community1] + size[community2]
            parent[community2] = community1


if __name__ == '__main__':
    N, M = sys.stdin.readline().split()
    N, M = int(N), int(M)
    size = [1] * (N+1)
    parent = [i for i in range(N+1)]
    q = int(sys.stdin.readline())
    for _ in range(q):
        line = sys.stdin.readline().split()
        if line[0] == 'A':
            x, y = int(line[1]), int(line[2])
            union(parent, size, x, y, M)
        elif line[0] == 'E':
            x, y = int(line[1]), int(line[2])
            p1 = find(parent,  x)
            p2 = find(parent,  y)
            if p1 == p2:
                print('Yes')
            else:
                print('No')
        else:
            com = int(line[1])
            print(size[find(parent, com)])
