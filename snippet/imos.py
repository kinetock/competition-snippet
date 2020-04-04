# https://atcoder.jp/contests/abc106/tasks/abc106_d


n,m,q = map(int, input().split())
grid = [[0 for i in range(n+1)] for _ in range(n+1)]

for i in range(m):
    l,r = map(int, input().split())
    grid[l][r] += 1

for i in range(n+1):
    for j in range(n+1):
        grid[i][j] += grid[i][j - 1]
for i in range(n+1):
    for j in range(n+1):
        grid[i][j] += grid[i - 1][j]

for _ in range(q):
    l,r = map(int, input().split())
    print(grid[r][r] + grid[l - 1][l - 1] - grid[l - 1][r] - grid[r][l - 1])
