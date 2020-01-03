import sys
sys.setrecursionlimit(100000)

def unite(par, i, j):
    j = get_par(par, j)
    par[j] = get_par(par, i)
    return

def get_par(par, p):
    if par[p] is None:
        return p
    par[p] = get_par(par, par[p])
    return par[p]

def kruskal(edges, n):
    par = [None] * n
    cost = 0

    edges.sort(key=lambda x:x[0], reverse=True)
    for _ in range(n-1):
        c, u, v = edges.pop()
        if get_par(par, u) == get_par(par, v):
            continue
        unite(par, u, v)
        cost += c

    return cost

n = int(input())
points = []
edges = []
for i in range(n):
    x,y = map(int, input().split())
    points.append([x,y,i])

points.sort(key=lambda x:x[0])
for i in range(n-1):
    edges.append((abs(points[i][0] - points[i+1][0]), points[i][2], points[i+1][2]))
points.sort(key=lambda x:x[1])
for i in range(n-1):
    edges.append((abs(points[i][1] - points[i+1][1]), points[i][2], points[i+1][2]))

print(kruskal(edges, n))
