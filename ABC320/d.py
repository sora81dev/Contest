N, M = map(int, input().split())
coordinates = [(0, 0)] * N  # 各人の座標を初期化

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1  # 0-based indexに変更
    B -= 1  # 0-based indexに変更

    # 横方向と縦方向の移動量を計算
    Xi = coordinates[A][0] - X
    Yi = coordinates[A][1] - Y

    # 人Bの座標を更新
    coordinates[B] = (Xi, Yi)

# 各人の座標を出力
for coord in coordinates:
    unique = True
    for other_coord in coordinates:
        if coord == other_coord:
            continue
        if coord == (other_coord[0] + coord[0], other_coord[1] + coord[1]):
            unique = False
            break
    if unique:
        print(coord[0], coord[1])
    else:
        print("undecidable")
