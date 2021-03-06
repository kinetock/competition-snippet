from scipy.sparse.csgraph import dijkstra as di
from itertools import permutations

n,m,r = map(int, input().split())
r = [int(i)-1 for i in input().split()]
route = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    a,b,c = map(int, input().split())
    route[a-1][b-1] = route[b-1][a-1] = c

# 要素はfloat なので注意
p_route = di(route)

mn = float('InF')
for perm in permutations(r):
    tmp = 0
    for i in range(len(perm)-1):
        tmp += p_route[perm[i]][perm[i+1]]
    if tmp < mn:
        mn = tmp

print(int(mn))