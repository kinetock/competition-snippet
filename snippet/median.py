N = int(input())
A = []
for i,a in enumerate(input().split()):
  A.append(int(a)-(i+1))
A.sort()
if N % 2 :
    print(-1*sum(A[:N//2]) + sum(A[N//2+1:]))
else:
    print(-1*sum(A[:N//2]) + sum(A[N//2:]))
