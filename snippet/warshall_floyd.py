# https://atcoder.jp/contests/abc022/tasks/abc022_c

from itertools import product

inf = float('INF')
def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    # [print(i) for i in d]

def initialize_warshall(n):
    g = [[inf for i in range(n)] for i in range(n)]
    for i in range(n):
        g[i][i] = 0
    return g

n,m = map(int,input().split())
graph = initialize_warshall(n)

start = {}
for i in range(m):
    u,v,l = map(int,input().split())
    u -= 1
    v -= 1
    if 0 == u:
        start[v] = l
    elif 0 == v:
        start[u] = l
    else:
        graph[u][v] = graph[v][u] = l

warshall_floyd(graph, n)
ans = inf
flag = False
for u,v in product(start.keys(), repeat=2):
    if u == v:
        continue
    cost = graph[u][v] + start[u] + start[v]
    if ans > cost:
        ans = cost
        flag = True
print(ans if flag else -1)
