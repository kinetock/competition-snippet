def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i % 1000000007
    return ans