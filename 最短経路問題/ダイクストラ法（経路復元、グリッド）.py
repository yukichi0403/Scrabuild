import heapq

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]


def dijkstra(grid, before, sx, sy, gx, gy):
    open_list = []
    heapq.heapify(open_list)

    closed = set()

    # ４つ目の引数は１つ前の状態を保持するもの
    initial_state = (sx, sy, grid[sy][sx], before)
    heapq.heappush(open_list, initial_state)

    while open_list:
        x, y, cost, before = heapq.heappop(open_list)

        if x == gx and y == gy:
            return cost, before

        if (x, y) in closed:
            continue

        closed.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue

            ncost = cost + grid[ny][nx]
            # before配列を更新して親セルの座標を格納
            before[ny][nx] = (x, y)
            heapq.heappush(open_list, (nx, ny, ncost, before))


# １つ前の地点を保持する配列を定義
before = [[(-1, -1)] * w for _ in range(h)]

# 最小コストを出力
cost, before = dijkstra(grid, before, 0, 0, w - 1, h - 1)
print(cost)

# 経路復元のコード
cur_y, cur_x = h - 1, w - 1  # 終点から始める
tour = [(cur_y, cur_x)]
while cur_x != -1 or cur_y != -1:
    cur_y, cur_x = before[cur_y][cur_x]
    tour.append((cur_y, cur_x))

# 最後のマイナス１を削除
tour.pop()

# 経路を出力
for t in tour[::-1]:
    y, x = t
    y += 1
    x += 1
    print(y, x)
