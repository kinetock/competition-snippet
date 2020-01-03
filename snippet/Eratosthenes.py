# https://atcoder.jp/contests/abc084/tasks/abc084_d

from itertools import accumulate

def eratosthenes(mx):
    array = [1 for _ in range(mx)]
    array[0] = array[1] = 0
    for i in range(4, mx, 2):
        array[i] = 0
    for i in range(3, mx, 2):
        if not array[i]:
            continue
        for j in range(i+i, mx, i):
            array[j] = 0
    return array

q = int(input())
l,r = [], []
for i in range(q):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)

mx = max(r)
array = eratosthenes(mx + 1)
prime = [1 if i % 2 == 1 and array[i] and array[(i+1) // 2] else 0 for i in range(mx + 1)]
acc = list(accumulate(prime))

for i in range(q):
    print(acc[r[i]] - acc[l[i]-1])
