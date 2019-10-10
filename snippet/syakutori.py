N,K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
right = 0
sum_val = 0
for left in range(N+1):
    while sum_val < K:
        if right == N:
            break
        else:
            right += 1
            sum_val += A[right]
    if sum_val < K:
        break
    cnt += (N - right + 1)
    sum_val -= A[left]
print(cnt)
