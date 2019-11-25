
def unite(par, i, j):
    j = get_par(par, j)
    par[j] = get_par(par, i)

def get_par(par, p):
    while par[p] != p:
        p = par[p]
    return par[p]

n,m,W = map(int, input().split())
v,w = [0],[0]
for _ in range(n):
    a,b = map(int, input().split())
    w.append(a)
    v.append(b)

par = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    if v[a] == 0:
        a = get_par(par, a)
    else :
        par[a] = a
    if v[b] == 0:
        b = get_par(par, b)
    else :
        par[b] = b
    unite(par, a, b)
    v[a] += v[b]
    w[a] += w[b]
    v[b],w[b] = 0,0

tank = [0 for _ in range(W+1)]
for i in range(n+1):
    if w[i] > W:
        continue
    for j in range(w[i], W+1)[::-1]:
        tank[j] = max(tank[j], tank[j-w[i]] + v[i])

print(tank[W])
