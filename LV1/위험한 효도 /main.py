from sys import stdin

a, b, d = map(int, stdin.readline().strip().split())
time = 0
pos = d
flag = True

while True:
    if not flag and pos == d:
        print(time)
        break
    if flag:
        pos -= a

        # 터치 O
        if pos <= 0:
            time += (a + pos)
            pos = 0
            flag = not flag
        else:
            time += (a+b)
    else:
        pos += b
        if pos >= d:
            time += (b -(pos - d))
            pos = d
        else:
            time += (b + a)
