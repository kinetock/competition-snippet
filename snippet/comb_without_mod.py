# https://atcoder.jp/contests/abc057/tasks/abc057_d

from operator import mul
from functools import reduce
from collections import Counter
from itertools import accumulate

def comb(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

n,a,b = map(int, input().split())
v = list(map(int, input().split()))
c = Counter(v)
keys = sorted(c.keys(), reverse=True)
acc = [0] + list(accumulate([c[k] for k in keys]))
costs = [0] + list(accumulate([c[k]*k for k in keys]))

d = []
for lim in range(a,b+1):
    for i,k in enumerate(keys):
        if acc[i+1] >= lim:
            d.append((costs[i] + (lim - acc[i]) * k, lim, comb(c[k], lim - acc[i])))
            break
e = sorted([[x[0] / x[1],x[2]] for x in d], reverse=True)
cnt = 0
mx = e[0][0]
i =0
while i < len(e) and mx <= e[i][0]:
    cnt += e[i][1]
    i += 1

print('{:.8f}'.format(mx))
print(cnt)
