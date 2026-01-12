from collections import deque, defaultdict
import sys


def solve(adj):
    STEPS, COST = 0, 1
    min_cost = {'English': (0,0)}
    q = deque([('English', 0)])

    while q:
        cur, steps = q.popleft()
        for nei, nei_cost in adj[cur]:
            if nei not in min_cost:
                min_cost[nei] = (steps + 1, nei_cost)
                q.append((nei, steps+1))
            if nei in min_cost and min_cost[nei][STEPS] >= steps + 1:
                    min_cost[nei] = (steps+1, min(nei_cost, min_cost[nei][COST]))
    return min_cost


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    sys.stdin.readline()
    adj = defaultdict(list)
    for _ in range(m):
        frm, to, cost = sys.stdin.readline().split()
        adj[frm].append((to, int(cost)))
        adj[to].append((frm, int(cost)))
    min_cost = solve(adj)
    if len(min_cost)-1 != n:
        print('Impossible')
    else:
        total = 0
        for lang, (steps, cost) in min_cost.items():
            total += cost
        print(total)
