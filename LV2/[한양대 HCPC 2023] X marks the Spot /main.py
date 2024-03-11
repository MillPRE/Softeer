from sys import stdin

n = int(stdin.readline())
result = ''

for _ in range(n):
    S, T = stdin.readline().strip().split()

    for idx, s in enumerate(S):
        if s == "x" or s =="X":
            result += T[idx]
            break

print(result.upper())

# 문자열 연결
# + -> list append join 이 속도가 더 빠르다