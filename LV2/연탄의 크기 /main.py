from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))

max_count = 0

for i in range(2, 101):
    count = 0

    for a in arr:
        if a % i == 0:
            count += 1
    if max_count < count:
        max_count = count

print(max_count)