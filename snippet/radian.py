# https://atcoder.jp/contests/abc144/tasks/abc144_d

from math import atan, degrees
a,b,x = map(int, input().split())
if a**2 * b / 2 < x:
    x = a**2 * b - x
    print('{:.10f}'.format(degrees(atan(x*2 / a/a/a ))))
else:
    print('{:.10f}'.format(90-degrees(atan(2 * x / a / b / b ))))
