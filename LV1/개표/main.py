from sys import stdin
import math

N = int(stdin.readline())
result = ""
for j in range(N):
    num = int(stdin.readline())
    tmp = ""
    if num // 5 > 0:
        for i in range(math.floor(num//5)):
            tmp += "++++" if i == math.floor(num//5)-1 else "++++ "
    if len(tmp) > 0 and num % 5 > 0:
        tmp += " "
    for i in range(num % 5):
        tmp += "|"

    if j < N-1:
        result += (tmp + "\n")
    else:
        result += tmp
print(result)