def dfs(grid, start, wall):
    stack = []
    push, pop = stack.append, stack.pop
    push(start)
    grid[start[0]][start[1]] = wall
    dxy = [(0,1), (0,-1), (1,0), (-1,0)]
    while stack:
        h,w = pop()
        for dx,dy in dxy:
            x, y = w+dx, h+dy
            if grid[y][x] == wall:
                continue
            if grid[y][x] == 'g':
                return True
            push((y,x))
            grid[y][x] = wall
    return False

h,w = map(int, input().split())
wall = '#'
edges = [wall] * (w+2)
grid = [edges]
for i in range(h):
    s = input()
    grid.append([wall] + list(s) + [wall])
    if 's' in s:
        start = (i+1, s.index('s')+1)
grid.append(edges)
print('Yes' if dfs(grid, start, wall) else 'No')
