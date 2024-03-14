from sys import stdin

rand = []
rand_height = [[1,1,1], [2,2,2], [3,3,3]]
diff = []

for _ in range(3):
    rand.append(list(map(int, stdin.readline().strip().split())))

for i in range(3):
    # 가로
    row = rand[i]
    # 세로
    col = [rand[0][i], rand[1][i], rand[2][i]]

    # print(row)
    # print(col)

    for j in range(3):
        height = rand_height[j] # ex) [1,1,1]
        col_cnt = 0
        row_cnt = 0

        for k in range(3):
            row_cnt += abs(row[k] - height[k])
            col_cnt += abs(col[k] - height[k])
        # print(row_cnt)
        # print(col_cnt)
        diff.append(row_cnt)
        diff.append(col_cnt)

print(min(diff))