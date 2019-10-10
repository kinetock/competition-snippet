# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d

import heapq
from itertools import accumulate
inf = float('inf')

def dijkstra(ad_lst, n, s):
    costs = [inf for i in range(n+1)]
    costs[s], Q = 0, []
    heapq.heappush(Q, [costs[s], s])

    while(Q != []):
        c, u = heapq.heappop(Q)
        for v, c in ad_lst[u].items():
            if costs[u] + c < costs[v]:
                heapq.heappush(Q, [costs[u] + c, v])
                costs[v] = costs[u] + c
    return costs

n,m,s,t, = map(int, input().split())

route_y = {i: {} for i in range(n+1)}
route_s = {i: {} for i in range(n+1)}
for i in range(m):
    u, v, a, b = map(int, input().split())
    route_y[u][v] = a
    route_y[v][u] = a
    route_s[u][v] = b
    route_s[v][u] = b

cost_y = dijkstra(route_y, n, s)
cost_s = dijkstra(route_s, n, t)
result = list(accumulate([y+s for y,s in zip(cost_y, cost_s)][::-1], min))
yen = 10**15
[print(yen-result[i]) for i in range(n-1, -1, -1)]
