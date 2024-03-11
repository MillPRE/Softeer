from sys import stdin

A, B = map(int, stdin.readline().strip().split())

if A == B:
    print('same')
else:
    print('A') if A > B else print('B')