# https://atcoder.jp/contests/abc079/tasks/abc079_d

from collections import Counter
from functools import reduce

# 行列(パス無し)は inf で初期化
inf = float('INF')
def warshall(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

h,w = map(int,input().split())
magic = [list(map(int,input().split())) for _ in range(10)]
counter = Counter()
[counter.update(Counter(map(int, input().split()))) for _ in range(h)]
warshall(magic, 10)
print(reduce(lambda x,y:x+y, [magic[k][1] * v for k,v in counter.items() if k > -1]))
