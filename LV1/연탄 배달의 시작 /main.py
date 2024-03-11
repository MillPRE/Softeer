from sys import stdin
n = int(stdin.readline())
town = list(map(int, stdin.readline().strip().split()))
diff_min = 1000000
diff_count = 0

for i in range(n-1):
    diff = town[i+1] - town[i]
    if diff < diff_min:
        diff_min = diff
        diff_count = 1
    elif diff == diff_min:
        diff_count += 1

print(diff_count)