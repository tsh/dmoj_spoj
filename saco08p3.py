from collections import deque, defaultdict
import heapq
import sys


def solve(adj, stores, stop):
    seen = set()
    seen.add((1, False))
    min_len = None
    number_of_ways = 0
    h = [(0, 1, False)]

    while h:
        cost, node, cur_have_cookie = heapq.heappop(h)
        if node == stop and cur_have_cookie:
            if min_len is None:
                min_len = cost
                number_of_ways += 1
            elif cost == min_len:
                number_of_ways += 1
            elif cost > min_len:
                print(f'{min_len} {number_of_ways}')
                return
        for nei, nei_cost in adj[node]:
            nei_have_cookies = False
            if nei in stores:
                nei_have_cookies = True
            have_cookie = cur_have_cookie or nei_have_cookies
            if (nei, have_cookie) in seen:
                continue
            heapq.heappush(h, (cost+nei_cost, nei, have_cookie))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    adj = defaultdict(list)
    for frm in range(N):
        line = sys.stdin.readline().split()
        for to in range(len(line)):
            if frm == to:
                continue
            adj[frm+1].append((to+1, int(line[to])))
    M = int(sys.stdin.readline())
    stores = set(map(int, sys.stdin.readline().split()))
    solve(adj, stores, N)
