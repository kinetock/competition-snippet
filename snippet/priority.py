from heapq import heappush, heappop

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    def push(self, value):
        heappush(self.queue, value)
    def pop(self):
        return heappop(self.queue)
    def __len__(self):
        return len(self.queue)
    def __contains__(self, item):
        return item in self.queue

N, K = map(int, input().split())
queue = PriorityQueue()
for i in range(N):
    a,b = map(int, input().split())
    queue.push([a,b])

time = 0
while len(queue) > 0 and K > 0:
    a,b = queue.pop()
    time += a
    K -= 1
    queue.push([a+b,b])
    #print(a, b, K)
print(time)
