# https://atcoder.jp/contests/abc144/tasks/abc144_e

def binary_search(a, f, target, left, right):
    ans = a[-1] * f[-1]
    while left + 1 < right:
        mid = (left+right)//2
        cost = 0
        for aa,ff in zip(a,f):
            if ff > mid:
                cost += aa
            elif aa - mid // ff > 0:
                cost += aa - mid // ff
        if cost > target:
            left = mid
        else:
            right = mid
    return right

n,k = map(int,input().split())
a = sorted(map(int, input().split()), reverse=True)
f = sorted(map(int, input().split()))
target = binary_search(a,f,k,-1,max(a) * max(f))
mx = 0
for aa, ff in zip(a,f):
    if ff > target:
        aa = 0
    elif aa - target // ff > 0:
        aa = (target // ff)
    if mx < aa * ff:
        mx = aa * ff
print(mx)
