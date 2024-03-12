from sys import stdin

# M : 비밀 조작 버튼 수
# N : 사용자 버튼 수
# K : 자판기 버튼의 수
M, N, K = map(int, stdin.readline().split())
SECRET = stdin.readline().strip()
USER = stdin.readline().strip()

if USER.find(SECRET) != -1:
    print("secret")
else:
    print("normal")
