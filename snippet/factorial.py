def factorial(n):
    ans = 1
    mod = 10**9 + 7
    for i in range(2, n + 1):
        ans = ans * i % mod
    return ans
