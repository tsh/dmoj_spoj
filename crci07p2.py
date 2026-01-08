from collections import defaultdict
from functools import cmp_to_key
from heapq import heappush, heappop
import sys

sys.stdin.readline()
cost = [float('inf')]
for line in sys.stdin:
    c = int(line)
    cost.append(c)

memo = {
}
def dp(prev_jump, i):
    if i <= 0 or i >= len(cost):
        return float('inf')
    if i == len(cost)-1:
        return cost[len(cost)-1]
    if (prev_jump, i) in memo:
        return memo[(prev_jump, i)]
    forward = dp(prev_jump+1, i+prev_jump+1)
    back = dp(prev_jump, i-prev_jump)
    res = cost[i] + min(forward, back)
    memo[(prev_jump, i)] = res
    return res
print( dp(1, 2))
