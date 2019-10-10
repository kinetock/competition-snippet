def is_bipartite(graph, start):
    stack = [start]
    visited = [-1] * (len(graph)+1)
    visited[start] = 0
    while stack:
        u = stack.pop()
        for v,w in graph[u].items():
            if visited[v] != -1:
                continue
            visited[v] = (visited[u] ^ 1) if w % 2 else visited[u]
            stack.append(v)
    return visited

n = int(input())
graph = {}

for i in range(n-1):
    u,v,w = map(int , input().split())
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    graph[v][u] = w

[print(color) for color in is_bipartite(graph, 1) if color > -1]
