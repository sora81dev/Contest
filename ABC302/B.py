H, W = map(int, input().split())

grid = []
for _ in range(H):
    row = input()
    grid.append(row)

# 各方向の移動ベクトル
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

# マス目の各マスを順番にチェック
for i in range(H):
    for j in range(W):
        if grid[i][j] == 's':
            # 各方向に対して5連続の文字列が現れるかをチェック
            for dx, dy in directions:
                x, y = i, j
                found = True
                for _ in range(4):
                    x += dx
                    y += dy
                    if not (0 <= x < H and 0 <= y < W and grid[x][y] == 'n' or grid[x][y] == 'u' or grid[x][y] == 'k' or grid[x][y] == 'e'):
                        found = False
                        break
                if found:
                    # 条件を満たす場所が見つかったら出力して終了
                    print(i + 1, j + 1)
                    exit()
