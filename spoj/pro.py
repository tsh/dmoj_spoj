import heapq
import sys


days = int(sys.stdin.readline())
min_heap = []
max_heap = []
is_used = set()
id_ = 0
res = 0
for _ in range(days):
    line = list(map(int, sys.stdin.readline().split()[1:]))
    for el in line:
        heapq.heappush(min_heap, (el, id_))
        heapq.heappush(max_heap, (-el, id_))
        id_ += 1

    max_val, max_id = heapq.heappop(max_heap)
    while max_id in is_used:
        max_val, max_id = heapq.heappop(max_heap)
    max_val = -max_val

    min_val, min_id = heapq.heappop(min_heap)
    while min_id in is_used:
        min_val, min_id = heapq.heappop(min_heap)

    is_used.add(min_id)
    is_used.add(max_id)

    res += max_val - min_val
print(res)
