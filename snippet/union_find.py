def unite(par, i, j):
    j = get_par(par, j)
    par[j] = get_par(par, i)

def get_par(par, p):
    while par[p] != None:
        p = par[p]
    return par[p]

N = int(input())
points = []
edges = []
for i in range(N):
    x,y = map(int, input().split())
    points.append([x,y,i])
points.sort()
for i in range(N-1):
    edges.append((abs(points[i][0] - points[i+1][0]), points[i][2], points[i+1][2]))
points.sort(key=lambda x:x[1])
for i in range(N-1):
    edges.append((abs(points[i][1] - points[i+1][1]), points[i][2], points[i+1][2]))
edges.sort(key=lambda x:x[0], reverse=True)

par = [None] * N
cost = 0
count = 0
points.sort()
while count < N - 1:
    c, i, j = edges.pop()
    if get_par(par, i) == get_par(par, j):
        continue
    unite(points, i, j)
    cost += c
    count += 1
print(cost)
