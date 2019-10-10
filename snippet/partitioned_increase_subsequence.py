N = int(input())
A = list(map(int, input().split()))+[10**9]
ans = 0
left = 0
for i in range(N):
    if A[i-1] >= A[i]:
        left = i
    ans += i-left+1
print(ans)
