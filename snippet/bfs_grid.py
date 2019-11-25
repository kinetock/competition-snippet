from collections import deque

def bfs(grid, sy, sx, target, wall):
    grid[sy][sx] = wall
    queue = deque([])
    queue.append([sy, sx, 0])
    dxy = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        y,x,cnt = queue.popleft()
        for dy, dx in dxy:
            y_,x_ = y+dy,x+dx
            if [y_, x_] == target:
                return cnt+1
            if grid[y_][x_] == wall:
                continue
            queue.append([y_,x_,cnt+1])
            grid[y_][x_] = wall
    return False

h,w = map(int, input().split())
gy,gx = map(int, input().split())
wall = '#'
start='s'
edges = [wall for i in range(w+2) ]
grid = [edges]
for i in range(1,h+1):
    S = [wall]+list(input().strip())+[wall]
    if 's' in S:
        sy,sx=i,S.index('s')
    grid.append(S)
grid.append(edges)

print(bfs(grid, sy, sx, [gy,gx], wall))
