import sys
import random

"""
Las Vegas algo
"""

def solve(bottles, caps):
    if len(caps) == 0:
        return
    small_bottle_pile = []
    large_bottle_pile = []
    small_caps_pile = []
    large_caps_pile = []

    pivot_cap = random.choice(caps)
    for bottle in bottles:
        print(f'0 {pivot_cap} {bottle}')
        resp = int(sys.stdin.readline())
        if resp == 0:
            match_bottle = bottle
        elif resp == 1:
            # cap is too large for the bottle
            small_bottle_pile.append(bottle)
        elif resp == -1:
            # cap is too small for the bottle
            large_bottle_pile.append(bottle)

    for cap in caps:
        print(f'0 {cap} {match_bottle}')
        resp = int(sys.stdin.readline().strip())
        if resp == 1:
            # cap is too large
            large_caps_pile.append(cap)
        elif resp == -1:
            small_caps_pile.append(cap)
    solve(small_bottle_pile, small_caps_pile)
    print(f'1 {pivot_cap} {match_bottle}')
    solve(large_bottle_pile, large_caps_pile)


N = int(sys.stdin.readline())
# fill starting from 1
bottles = [i+1 for i in range(N)]
caps = [i+1 for i in range(N)]
solve(bottles, caps)
