# https://atcoder.jp/contests/arc061/tasks/arc061_b
H,W,N = map(int, input().split())

grid = {}
for _ in range(N):
    a,b = map(int, input().split())

    for i in range(3):
        for j in range(3):
            if 0 < a-i <= H-2 and 0 < b-j <= W-2:
                if a-i not in grid:
                    grid[a-i] = {}
                if b-j not in grid[a-i]:
                    grid[a-i][b-j] = 0
                grid[a-i][b-j] += 1
ans = [0 for i in range(10)]
for a,bb in grid.items():
    for cnt in bb.values():
        ans[cnt] += 1
    
print((H-2)*(W-2) - sum(ans))
for i in range(1,10):
    print(ans[i])
