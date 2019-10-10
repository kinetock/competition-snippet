D,N = map(int, input().split())
days = [int(input()) for i in range(D)]
clothes = [list(map(int, input().split())) for i in range(N)]

temp = [{} for i in range(60+1)]
for i,cloth in enumerate(clothes):
    a,b,c = cloth
    for j in range(a,b+1):
        temp[j][i] = 1

charm = []
for i in range(N):
    charm.append([])
    for j in range(N):
        charm[i].append(abs(clothes[i][2] - clothes[j][2]))

memo = [{} for i in range(D)]
for i in temp[days[0]].keys():
    memo[0][i] = 0
for i in range(1,D):
    for j in temp[days[i]].keys():
        c = max([charm[j][k] + memo[i-1][k] for k in temp[days[i-1]].keys()])
        memo[i][j] = c
print(max(memo[D-1].values()))