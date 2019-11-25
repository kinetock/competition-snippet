# https://atcoder.jp/contests/bitflyer2018-final-open/tasks/bitflyer2018_final_b

from itertools import accumulate
import bisect
import sys

n,q = map(int,input().split())
x = sorted(map(int,input().split()))
acc = [0] + list(accumulate(x))

ans = []
for line in sys.stdin:
    c,d = map(int, line.split())
    a = bisect.bisect(x, c-d)
    m = bisect.bisect(x, c)
    b = bisect.bisect(x, c+d)
    ans.append((a+n-b)*d + c*(2*m-a-b) + acc[b] - 2*acc[m] + acc[a])
print(*ans)
# [print(i) for i in ans]
# print('\n'.join(map(str, ans)))
