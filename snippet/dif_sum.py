N, M =map(int, input().split())
L = [0 for i in range(N+1)]
R = [0 for i in range(N+1)]
for i in range(M):
    l,r = map(int, input().split())
    L[l] += 1
    R[r] += 1
cnt = 0
tmp = 0
for i in range(N+1):
    tmp += L[i]
    if tmp == M:
        cnt += 1
    tmp -= R[i]
print(cnt)
