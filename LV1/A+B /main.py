from sys import stdin

n = int(stdin.readline())
for i in range(n):
    a, b = map(int, stdin.readline().strip().split())
    print(f'Case #{i+1}: {a+b}')