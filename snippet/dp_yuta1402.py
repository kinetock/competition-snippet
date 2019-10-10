# https://atcoder.jp/contests/code-festival-2018-final-open/tasks/code_festival_2018_final_a

dp = [{} for _ in range(1540+1)]

n, m = map(int, input().split())
ans = 0

for i in range(m):
    a, b, l = map(int, input().split())
    if l > 1540:
        continue
    if a in dp[l]:
        ans += dp[l][a]
    if b in dp[l]:
        ans += dp[l][b]

    if a not in dp[2540 - l]:
        dp[2540 - l][a] = 0
    if b not in dp[2540 - l]:
        dp[2540 - l][b] = 0

    dp[2540 - l][a] += 1
    dp[2540 - l][b] += 1

print(ans)
