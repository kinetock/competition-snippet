# https://atcoder.jp/contests/abc138/tasks/abc138_d

import sys
input = sys.stdin.readline

def dfs(lst, start, ans):
    queue = [start]
    visited = [False] * len(ans)
    visited[start] = True

    while queue:
        parent = queue.pop()
        for child in lst[parent]:
            if visited[child]:
                continue
            visited[child] = True
            ans[child] += ans[parent]
            queue.append(child)

    print(*ans)

n,q = map(int, input().split())
start = 0

tree = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

ans = [0]*n
for _ in range(q):
    p, x = map(int,input().split())
    ans[p-1] += x
dfs(tree, start, ans)
