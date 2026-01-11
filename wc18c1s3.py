from collections import deque
import sys


def solve(H,J,powder):
    # TODO: 1-0 bfs
    seen = set()
    q = deque([(0,0)])
    seen.add(0)
    while q:
        jump, cur = q.popleft()
        if cur >= H:
            print(jump)
            return
        if cur + J not in seen and cur+J not in powder:
            q.append((jump+1, cur+J))
            seen.add(cur+J)
        for i in range(cur, -1, -1):
            if i not in seen and i not in powder:
                q.append((jump+1, i))
                seen.add(i)
    print(-1)

if __name__ == '__main__':
    hjn = sys.stdin.readline().split()
    H, J, N = int(hjn[0]), int(hjn[1]), int(hjn[2])
    powder = set()
    for _ in range(N):
        line = sys.stdin.readline().split()
        r = set(range(int(line[0]), int(line[1])+1))
        powder.update(r)
    solve(H, J, powder)
