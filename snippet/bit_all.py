from itertools import permutations as perm

N = int(input())
A = list(map(int, input().split()))

pm = {0:1, 1:-1}
p = {0:'+', 1:'-'}
ans = 0
for i in range(1<<(N-2)):
    tmp = A[0]
    for j in range(N-2):
        tmp += A[j+1] * pm[i & (1<<j) == 0]
        if tmp > 20 or tmp < 0:
            break
    else:
        if tmp == A[-1]:
            ans += 1
print(ans)



