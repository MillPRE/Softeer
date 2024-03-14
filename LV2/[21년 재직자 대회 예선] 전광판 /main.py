from sys import stdin

T = int(stdin.readline())
N = 5
# 위, 오른쪽 위, 오른쪽 아래, 아래, 왼쪽 아래, 왼쪽 위, 가운데
state = {
    "1": ['0', '1', '1', '0', '0', '0', '0'],
    "2": ['1', '1', '0', '1', '1', '0', '1'],
    "3": ['1', '1', '1', '1', '0', '0', '1'],
    "4": ['0', '1', '1', '0', '0', '1', '1'],
    "5": ['1', '0', '1', '1', '0', '1', '1'],
    "6": ['1', '0', '1', '1', '1', '1', '1'],
    "7": ['1', '1', '1', '0', '0', '1', '0'],
    "8": ['1', '1', '1', '1', '1', '1', '1'],
    "9": ['1', '1', '1', '1', '0', '1', '1'],
    "0": ['1', '1', '1', '1', '1', '1', '0'],
    "off0" : ['0', '0', '0', '0', '0', '0', '0']
}

# bin(int("".join(dict["2"]), 2))

for _ in range(T):
    cnt = 0
    before, after = stdin.readline().strip().split()

    after = list(after)
    before = list(before)

    _max = max(len(before), len(after))

    # 0 채우기
    if len(before) < 5:
        before = ["off0" for i in range((5 - len(before)))] + before

    if len(after) < 5:
        after = ["off0" for i in range((5 - len(after)))] + after

    for i in range(N):
        # print(before[i], after[i])
        b = before[i]
        a = after[i]
        a_s = state[a]
        b_s = state[b]
        _cnt = 0
        for s in range(7):
            if a_s[s] != b_s[s]:
                cnt += 1
    print(cnt)