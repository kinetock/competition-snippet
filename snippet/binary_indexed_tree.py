# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j

# # add value at idx on bit O(logN)
# def add(bit_array, idx, val):
#     for i in range(idx, len(bit_array)):
#         # (i=idx;i<bit.length;i+=(i&-i)):
#         bit_array[i] += val


# # return sum [1,idx] O(logN)
# def sum(bit_array, idx):
#     ret = 0
#     for i in range(1, idx+1)[::-1]:
#         # (int i=idx;i>0;i-=(i&-i)) :
#         ret += bit_array[i];
#     return ret

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

n = int(input())
a = list(map(int, input().split()))
bit = Bit(max(a))
ans = 0
for i, p in enumerate(a):
    bit.add(p, 1)
    ans += i + 1 - bit.sum(p)

print(ans)
