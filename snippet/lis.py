# https://atcoder.jp/contests/abc038/tasks/abc038_d

import bisect

def lis(a, n):
    seq = [a[0][1]]
    for w,h in a[1:]:
        if h > seq[-1]:
            seq.append(h)
        else:
            j = bisect.bisect_left(seq, h)
            seq[j] = h
        # print(seq, (w,h))
    return len(seq)

n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[0], -x[1]))

print(lis(a,n))
