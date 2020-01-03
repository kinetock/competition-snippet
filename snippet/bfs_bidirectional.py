# https://atcoder.jp/contests/abc067/tasks/arc078_b

from collections import deque


def bfs(graph, stack, visited, times):
    cnt = 0
    while stack:
        a,cost = stack.popleft()
        if cost > times:
            stack.appendleft([a,cost])
            break
        for b in graph[a].keys():
            if not visited[b]:
                stack.append([b,cost+1])
                visited[b] += 1 
                cnt += 1
    return cnt

def bi_bfs(graph, start, goal):
    s_stack, g_stack = deque(), deque()
    s_stack.append([start,0])
    g_stack.append([goal, 0])
    visited = [0 for i in range(n+1)]
    visited[start] = visited[goal] = 1 
    s_cnt = g_cnt = 1
    times = 0

    while s_stack or g_stack:
        s_cnt += bfs(graph, s_stack, visited, times)
        g_cnt += bfs(graph, g_stack, visited, times)
        times += 1
    return s_cnt > g_cnt

n = int(input())
graph = {}
for i in range(n-1):
    a,b = map(int, input().split())
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = graph[b][a] = 1
print('Fennec' if bi_bfs(graph,1,n,n) else 'Snuke')
