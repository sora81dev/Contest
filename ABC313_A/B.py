def main():
    # 入力を受け取る
    N, M = map(int, input().split())

    # strength_mapを初期化
    strength_map = [[False] * N for _ in range(N)]

    # 強さに関する情報を入力し、strength_mapを更新する
    for _ in range(M):
        A, B = map(int, input().split())
        strength_map[A-1][B-1] = True
        strength_map[B-1][A-1] = True  # 逆向きの情報も更新

    # 推移律を考慮してstrength_mapを更新する
    for k in range(N):
        for i in range(N):
            for j in range(N):
                strength_map[i][j] = strength_map[i][j] or (strength_map[i][k] and strength_map[k][j])

    # 最強のプログラマーを特定する
    for i in range(N):
        if all(strength_map[i]):
            print(i + 1)  # 1-indexedで出力
            return

    # 最強のプログラマーが特定できない場合
    print(-1)

if __name__ == "__main__":
    main()
