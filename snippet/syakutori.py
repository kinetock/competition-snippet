# https://atcoder.jp/contests/abc098/tasks/arc098_b

n = int(input())
a = list(map(int, input().split()))

cnt = 0
right = 0
acc = a[0]
xor = a[0]
for left in range(n):
    while right < n:
        if right + 1 >= n or acc + a[right+1] != xor ^ a[right+1]:
            break
        right += 1
        acc += a[right]
        xor ^= a[right]
    if acc == xor:
        # print(left, right, acc, xor, cnt, right - left + 1)
        cnt += (right - left + 1)
    acc -= a[left]
    xor ^= a[left]
print(cnt)
