# https://atcoder.jp/contests/abc040/tasks/abc040_d

import sys
sys.setrecursionlimit(10**9)


def unite(par, i, j):
    j = get_par(par, j)
    par[j] = get_par(par, i)

def get_par(par, p):
    while par[p] != p:
        p = par[p]
    return par[p]

n,m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(m)]
road.sort(key=lambda x:x[2], reverse=True)
q = int(input())
vw = []
for i in range(q):
    v,w = map(int,input().split())
    vw.append((v,w,i))
vw.sort(key=lambda x:x[1], reverse=True)

ans = [0 for _ in range(q)]
cnt = [1 for _ in range(n+1)]
par = [i for i in range(n+1)]

pointer = 0
for v,w,i in vw:
    while pointer < m and road[pointer][2] > w:
        a,b,y = road[pointer]
        pointer += 1
        aa = get_par(par, a)
        bb = get_par(par, b)
        if aa == bb:
            continue
        # unite
        if cnt[aa] > cnt[bb]:
            par[bb] = aa
            cnt[aa] += cnt[bb]
        else:
            par[aa] = bb
            cnt[bb] += cnt[aa]

    ans[i] = cnt[get_par(par, v)]

[print(i) for i in ans]
# print(cnt)