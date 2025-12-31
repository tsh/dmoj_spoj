from collections import defaultdict
from functools import cmp_to_key
from heapq import heappush, heappop


import sys

def count(people, name, depth):
    if depth == 0:
        return 1
    c = 0
    for child in people[name]:
        c += count(people, child, depth-1)
    return c

def counter(people, d):
    c = defaultdict(int)
    for name in people:
        c[name] = count(people, name, d)
    return c

def process(records):
    people = defaultdict(list)
    for parent, children in records:
        people[parent].extend(children)
        for child in children:
            if child not in people:
                people[child] = []
    return people


def output(counter):
    out = sorted(counter.items(), key=lambda x:x[0])
    out = sorted(out, key=lambda x:x[1], reverse=True)
    i = 0
    while i < 3 and i < len(out) and out[i][1] > 0:
        print(f'{out[i][0]} {out[i][1]}')
        i+=1
        while i < len(out) and out[i][1] == out[i-1][1]:
            print(f'{out[i][0]} {out[i][1]}')
            i+= 1


num_cases = int(sys.stdin.readline())
for case in range(1, num_cases+1):
    n, d = sys.stdin.readline().split()
    n, d = int(n), int(d)
    records = []
    for i in range(n):
        line = sys.stdin.readline().split()
        parent, children = line[0], line[2:]
        records.append([parent, children])
    people = process(records)
    c = counter(people, d)
    print(f'Tree {case}:')
    output(c)
    if case < num_cases:
        print('\n', end='')
