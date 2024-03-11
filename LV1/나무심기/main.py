from sys import stdin

n = int(stdin.readline())
F = list(map(int, stdin.readline().strip().split()))
minus = []
plus = []

if len(F) == 2:
    print(F[0] * F[1])
else:
    for f in F:
        if f < 0:
            minus.append(-f)
        else:
            plus.append(f)
    minus_max = -1
    plus_max = -1

    minus.sort(reverse=True)
    plus.sort(reverse=True)

    if len(minus) >= 2:
        minus_max = minus[0] * minus[1]

    if len(plus) >= 2:
        plus_max = plus[0] * plus[1]

    print(max(minus_max, plus_max))
