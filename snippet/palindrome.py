def is_palindrome(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-(i+1)] and '.' not in [s[i], s[-(i+1)]]:
            return False
    return True

s = input()
t = '.'
if is_palindrome(s):
    print(0)
    exit()

for i in range(1,len(s)):
    s += '.'
    # print(s, is_palindrome(s))
    if is_palindrome(s):
        print(i)
        break
