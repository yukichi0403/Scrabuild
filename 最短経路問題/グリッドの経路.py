#幅
w = 10
#高さ
h = 8

x = 3
y = 4

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
        continue