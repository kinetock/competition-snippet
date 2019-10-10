N,M = map(int, input().split())
graph = {}
for i in range(M):
    a,b = map(int, input().split())
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = graph[b][a] = 1
