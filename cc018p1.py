from collections import defaultdict
from functools import cmp_to_key
from heapq import heappush, heappop
import sys

N = sys.stdin.readline()
geese = sys.stdin.readline()
geese_scores = list(map(int, sys.stdin.readline().split()))
hawks = sys.stdin.readline()
hawks_scores = list(map(int, sys.stdin.readline().split()))

memo = {}

def dp(gi, hi):
    if gi == len(geese) or hi == len(hawks):
        return 0
    if (gi, hi) in memo:
        return memo[(gi,hi)]

    if ((geese[gi] == 'W' and hawks[hi] == 'L' and geese_scores[gi] > hawks_scores[hi]) or
            (geese[gi] == 'L' and hawks[hi] == 'W' and geese_scores[gi]< hawks_scores[hi])):
        first = geese_scores[gi] + hawks_scores[hi] + dp(gi+1, hi+1)
    else:
        first = 0
    second = dp(gi+1, hi+1)
    third = dp(gi+1, hi)
    fourth = dp(gi, hi+1)
    res =  max(first, max(second,max(third, fourth)))
    memo[(gi,hi)] = res
    return res

print(dp(0,0))
