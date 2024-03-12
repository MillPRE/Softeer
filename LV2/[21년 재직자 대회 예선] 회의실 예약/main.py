from sys import stdin

n, m = map(int, stdin.readline().split())
room = {}

for _ in range(n):
    room[stdin.readline().strip()] = [0 for i in range(10)]

for _ in range(m):
    room_name, startH, endH = stdin.readline().split()
    startH = int(startH)
    endH = int(endH)

    for i in range(endH-startH):
        room[room_name][startH-9+i] = 1

room_names = list(room.keys())
room_names.sort()

for i in range(len(room_names)):
    name = room_names[i]
    print(f"Room {name}:")
    if room[name].count(0) == 1:
        print("Not available")
    else:
        time_cnt = 0
        times = []
        s = -1
        for idx in range(len(room[name])):
            time = idx + 9
            t = room[name][idx]
            if t == 0 and s == -1:
                s = time
            elif t == 1 and s > -1:
                if s < 10:
                    s = f"0{s}"
                times.append(f"{s}-{time}")
                time_cnt += 1
                s = -1
            elif t == 0 and idx == 9 and s > -1:
                if s < 10:
                    s = f"0{s}"
                times.append(f"{s}-{time}")
                time_cnt += 1
        print(f"{time_cnt} available:")
        for time in times:
            print(time)
    if i < n-1:
        print("-----")