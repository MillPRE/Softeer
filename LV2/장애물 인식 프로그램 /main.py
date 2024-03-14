from collections import deque
from sys import stdin

N = int(stdin.readline())
rand = []
count = []

for _ in range(N):
    rand.append(list(stdin.readline().strip()))

def bfs(rand, start, name):
    queue = [start]
    visited = []
    count.append(0)
    name = str(name)
    while len(queue) > 0 :

        position = queue.pop(0)
        if position not in visited:
            visited.append(position)
            if rand[position[0]][position[1]] == "1":
                rand[position[0]][position[1]] = name
                count[int(name) - 2] += 1
                top = (position[0] - 1, position[1])
                bottom = (position[0] + 1, position[1])
                right = (position[0], position[1] + 1)
                left = (position[0], position[1] - 1)

                for p in [top, bottom, right, left]:
                    if 0 <= p[0] < N and 0 <= p[1] < N:
                        queue.append(p)
    return rand

name = 2
while True:
    start = - 1
    for i in range(N):
        if rand[i].count('1') >= 1:
            start = (i, rand[i].index('1'))
            break
    if start == -1:
        break
    rand = bfs(rand, start, name)
    name += 1

print(rand)
print(len(count))
count.sort()
for c in count:
    print(c)
