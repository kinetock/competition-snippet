#https://atcoder.jp/contests/abc065/tasks/arc076_b

from heapq import heappush, heappop

def prim_heap(edges, n):
    visited = [False] * n
    heap = []
    start = 0
    for e in edges[start]:
        heappush(heap, e)
    visited[start] = True

    res = 0
    while heap:
        cost, v = heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        res += cost
        for c,u in edges[v]:
            if visited[u]:
                continue
            heappush(heap, (c,u))
    return res

n = int(input())
edges = []

for i in range(n):
    x,y = map(int,input().split())
    edges.append((x,y))

x = sorted(range(n), key=lambda i:edges[i][0])
y = sorted(range(n), key=lambda i:edges[i][1])
edge_list = [[] for _ in range(n)]
manhattan = lambda a,b: min(abs(a[0] - b[0]), abs(a[1] - b[1]))
for i in range(n):
    if i + 1 < n:
        edge_list[x[i]].append((manhattan(edges[x[i]], edges[x[i+1]]), x[i+1]))
        edge_list[x[i+1]].append((manhattan(edges[x[i]], edges[x[i+1]]), x[i]))
        edge_list[y[i]].append((manhattan(edges[y[i]], edges[y[i+1]]), y[i+1]))
        edge_list[y[i+1]].append((manhattan(edges[y[i]], edges[y[i+1]]), y[i]))

print(prim_heap(edge_list, n))

