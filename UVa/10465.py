import sys
"""
Input consists of several test cases. Each test case consists of three integers
m, n, t (0 < m, n, t < 10000). Input is terminated by EOF.

For each test case, print in a single line the maximum number of burgers
Homer can eat without having beer. If homer must have beer, then also
print the time he gets for drinking, separated by a single space. It is preferable that Homer drinks as
little beer as possible.

Sample Input
3 5 54
3 5 55

Sample Output
18
17
"""

def solve(m,n,t):
    dp = [None] * (t+1)
    dp[0] = 0
    for i in range(1, t+1):
        mback, nback = -1, -1
        if i >=m:
            mback = dp[i-m]
        if i >= n:
            nback = dp[i-n]

        if mback == -1 and nback == -1:
            dp[i] = -1
        else:
            dp[i] = max(mback, nback) + 1
    res = dp[t]
    if res >= 0:
        print(res)
    else:
        i = t-1
        res = dp[i]
        while res != -1:
            i -= 1
            res = dp[i]
        print(f'{res} {t-res}')

for line in sys.stdin.readlines():
    m,n,t = line.split()
    m,n,t = int(m),int(n),int(t)
    solve(m,n,t)
