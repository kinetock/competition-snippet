n,k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
right = 0
sum_val = 0
for left in range(n+1):
    while sum_val < k:
        if right == n:
            break
        else:
            right += 1
            sum_val += a[right]
    if sum_val < k:
        break
    cnt += (n - right + 1)
    sum_val -= a[left]
print(cnt)
