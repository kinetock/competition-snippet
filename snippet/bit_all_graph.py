#bid DP
N, M = map(int, input().split())

g = [[] for i in range(N)] #隣接リスト

for i in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

memo = {}
All_used = (1 << N) -1

def dfs(v, used):
    if used == All_used:
        return 1
    
    key = (v, used)
    if key in memo:
        return memo[key]
    
    ans = 0
    for u in g[v]:
        if (used >> u) & 1 == 1:
            continue
        
        used ^= (1 << u)
        ans += dfs(u, used)
        used ^= (1 << u)
        
    memo[key] = ans
    return ans

print(dfs(0, 1))
