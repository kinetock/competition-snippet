# https://atcoder.jp/contests/abc063/tasks/arc075_b

def binary_search(h, left, right, a,b):
    d = a-b
    while left + 1 < right:
        k = (left+right)//2
        c = cost(h,b,d,k)
        # print(left,right, k, cost)
        if c > k:
            left = k
        else:
            right = k
    return right

def cost(array,b,d,k):
    c = 0
    for i in array:
        tmp = i - k * b
        if tmp <= 0:
            continue
        c += (tmp + d - 1) // d
    return c

n,a,b = map(int,input().split())
h = []
cnt = 0
for _ in range(n):
    i = int(input())
    h.append(i)
    cnt += (i+a-1)//a
print(binary_search(h, -1, cnt+1,a,b))
