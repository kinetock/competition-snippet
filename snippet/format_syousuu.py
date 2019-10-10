from functools import lru_cache

@lru_cache(maxsize=None)
def p(i, prd):
    return i * prd

N,D = map(int, input().split())
A = {i:1 for i in range(1,6+1)}
print(A, A[4])
for i in range(1,N):
    tmp = {}
    for prd,cnt in A.items():
        for i in range(1,6+1):
            product = p(i,prd)
            if product not in tmp:
                tmp[product] = cnt
            else :
                tmp[product] += cnt
    A = tmp
cnt = 0
for key,value in A.items():
    if key % D == 0:
        cnt += value

print('{:.8f}'.format(cnt / 6**N))
