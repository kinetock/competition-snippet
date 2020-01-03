def bellman_ford(edges, start, n):
    costs = [float('INF')] * n
    # predecessors = [-1] * n
    costs[start]= 0

    for _ in range(n-1):
        for u,v,c in edges:
            if costs[v] > costs[u] + c:
                costs[v] = costs[u] + c
                # predecessors[v] = u

    ans = costs[-1]
    for u,v,c in edges:
        if costs[v] > costs[u] + c:
            costs[v] = costs[u] + c

    return -ans if costs[-1] == ans else 'inf'

n,m = map(int, input().split())
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a-1,b-1,-c))

print(bellman_ford(edges, 0, n))
