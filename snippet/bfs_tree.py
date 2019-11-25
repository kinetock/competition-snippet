#https://atcoder.jp/contests/abc146/tasks/abc146_d

from collections import deque


def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

def bfs(tree, idx, mx_color, n):
    queue = deque([])
    queue.append([idx, n, color+1])
    edge_color = {}
    visit = [False] * (n)
    visit[idx] = True

    while queue:
        parent,p,cc = queue.popleft()
        # print(parent, cc, '-', tree[parent])
        res_color =  my_index(tree[parent], p, -1)+1
        for i, child in enumerate(tree[parent]):
            if visit[child]:
                continue
            child_color = res_color if i+1 == cc else (i+1)
            edge_color[str(min(parent,child))+','+str(max(parent,child))] = child_color
            # print([child, child_color])
            queue.append([child, parent, child_color])
            visit[child] = True
    return edge_color

n = int(input())
tree = [[] for _ in range(n)]
edge = []
for _ in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
    edge.append(str(min(a,b))+','+str(max(a,b)))
color = max(len(i) for i in tree)

edge_color = bfs(tree, 0, color, n)
print(color)
#print(edge_color)
[print(edge_color[c]) for c in edge]
