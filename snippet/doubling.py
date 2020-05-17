# https://atcoder.jp/contests/abc167/tasks/abc167_d

def resolve():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    c = 1
    while k:
        if k & 1:
            c = a[c]
        na = [0] * (n+1)
        for i in range(n+1):
            na[i] = a[a[i]]
        a = na
        k >>= 1

    print(c)

if __name__ == '__main__':
    resolve()
