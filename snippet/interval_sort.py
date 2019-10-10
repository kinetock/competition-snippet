# https://atcoder.jp/contests/abc103/tasks/abc103_d 

N, M = map(int, input().split())
claim = []
for i in range(M):
	claim.append(list(map(int, input().split())))
claim.sort(key=lambda a:a[1])

ans = 0
inter = [-1,-1]
for land in claim:
	if inter[1] <= land[0]:
		inter = land
		ans += 1
	print(ans)


# ---------------------------
T = int(input())
word = 'kyoto'
for _ in range(T):
	s = input()
	s_len = len(s)
	count = 0
	while 0 <= s_len:
		tokyo_f = s[:s_len].rfind('tokyo')
		kyoto_f = s[:s_len].rfind('kyoto')
		s_len = max(tokyo_f, kyoto_f)
		if s_len >= 0:
			count += 1
	print(count)
