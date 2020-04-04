# https://atcoder.jp/contests/abc016/tasks/abc016_4

def judge_ientersected(ax, ay, bx, by, cx, cy, dx, dy):
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

    return tc * td < 0 and ta * tb < 0
    # return tc * td <= 0 and ta * tb <= 0 # 端点を含む場合

ax,ay,bx,by = map(int, input().split())
n = int(input())
xy = []
for _ in range(n):
    x,y = map(int,input().split())
    xy.append((x,y))
xy.append(xy[0])

cnt = 0
for i in range(n):
    u,v = xy[i+1],xy[i]

    if judge_ientersected(ax,ay,bx,by, u[0],u[1],v[0],v[1]):
        cnt += 1
print(cnt//2 + 1)
