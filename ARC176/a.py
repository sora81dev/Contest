def solve(n, m):
    # 各行と列にM個の1を書き込む
    grid = [[0] * n for _ in range(n)]
    for i in range(m):
        grid[i][i] = 1
    for i in range(n):
        for j in range(m):
            grid[i][j] = 1

    # 矛盾が生じないように、1を書き込む場所を調整する
    for i in range(n):
        # 行iにM個の1があるか確認する
        count = sum(grid[i])
        if count == m:
            continue

        # 行iにM個未満の1がある場合、調整する
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1
                for k in range(n):
                    if grid[k][j] == 1 and k != i:
                        grid[k][j] = 0
                        break
                break

    for j in range(n):
        # 列jにM個の1があるか確認する
        count = sum(row[j] for row in grid)
        if count == m:
            continue

        # 列jにM個未満の1がある場合、調整する
        for i in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1
                for k in range(n):
                    if grid[k][j] == 1 and k != i:
                        grid[k][j] = 0
                        break
                break

    # 出力
    print(m)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                print(i + 1, j + 1)

# 例: N = 5, M = 2
solve(5, 2)
