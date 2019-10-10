from collections import deque

def dfs(graph, start, goal):
    stack = deque()
    push, pop = stack.append, stack.pop
    visited = [False for i in range(N)]
    push(start)
    visited[start] = True
    
    while stack:
        a = pop()
        for b in graph[a].keys():
            if a in [start, goal] and b in [start, goal]:
                continue
            elif b == goal:
                return True
            elif not visited[b]:
                push(b)
    return False

N,M = map(int, input().split())
graph = {}
bridge = []
for i in range(M):
    a,b = map(int, input().split())
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = graph[b][a] = 1
    bridge.append([a,b])

ans = 0
for a,b in bridge:
    ans += dfs(graph, a, b)
print(ans)