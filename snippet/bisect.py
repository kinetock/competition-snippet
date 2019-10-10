import bisect
from itertools import accumulate

n = int(input())
a = sorted(map(int,input().split()))
b = sorted(map(int,input().split()))
c = sorted(map(int,input().split()))

ans = 0
b_sect = [0]
for i in range(n)[::-1]:
    b_sect.append(n-bisect.bisect_right(c,b[i]))
acc = list(accumulate(b_sect))[::-1]

for i in a:
    t = bisect.bisect_right(b,i)
    ans += acc[t]
print(ans)