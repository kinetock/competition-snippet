import fractions
import sys
import functools
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))
A.sort()
mx = 10 ** 9
idx = 0

print(test(A, N))

def test(A, N):
    if N < 3:
        return max(A)
    g = [[functools.reduce(fractions.gcd, A[i:i+3]),i] for i in range(N-3)]
    g.sort(key=lambda x:x[0])
    tmp = [fractions.gcd(i, i) for i in A[i:i+3]]
    A.remove(max(tmp))
    return fractions.reduce(fractions.gcd, A)
