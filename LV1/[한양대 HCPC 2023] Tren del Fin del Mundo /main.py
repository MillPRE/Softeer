from sys import stdin

n = int(stdin.readline())
train = []

for i in range(n):
    line = list(map(int, stdin.readline().strip().split()))
    train.append(line)

train.sort(key=lambda x: x[1])
print(train[0][0], train[0][1])