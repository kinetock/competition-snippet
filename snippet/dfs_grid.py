from collections import deque

def dfs(grid, start):
    stack = deque()
    push, pop = stack.append, stack.pop
    push(start)
    grid[start[0]][start[1]] = '#'
    dxy = [(0,1), (0,-1), (1,0), (-1,0)]
    while stack:
        h,w = pop()
        for dx,dy in dxy:
            x, y = w+dx, h+dy
            if grid[y][x] == '#':
                continue
            if grid[y][x] == 'g':
                return True
            push((y,x))
            grid[y][x] = '#'
    return False

H,W = map(int, input().split())
edges = ['#'] * (W+2)
grid = [edges]
for i in range(H):
    s = input()
    grid.append(['#'] + list(s) + ['#'])
    if 's' in s:
        start = (i+1, s.index('s')+1)
grid.append(edges)
print('Yes' if dfs(grid, start) else 'No')

