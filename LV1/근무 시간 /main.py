from sys import stdin

total = 0
for i in range(5):
    s, e = map(str, stdin.readline().split())
    sh, sm = map(int, s.split(":"))
    eh, em = map(int, e.split(":"))
    # print(sh, sm, eh, em)
    diff_h = eh - sh
    diff_m = em - sm
    # print(diff_h, diff_m)
    if diff_m < 0:
        diff_h -= 1
        diff_m += 60
    total += diff_m + (diff_h * 60)
    # print(diff_m + (diff_h * 60))

print(total)
