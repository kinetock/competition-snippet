from itertools import accumulate

def run_length(data, init):
    tmp = init
    cnt = 0
    for c in data:
        if tmp != c:
            length.append(cnt)
            cnt = 0
        tmp = c
        cnt += 1
    length.append(cnt)
    return length

n,m = map(int,input().split())
s = input()
if max(len(i) for i in s.split('0')) >= m:
    print(-1)
    exit()

if __name__ == "__main__":
    length = run_length(s, '')
    print(length)
