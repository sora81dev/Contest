def count_possible_positions(H, W, N, T, S):
    # 不時着したマスの座標を探す
    crash_row, crash_col = -1, -1
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'X':
                crash_row, crash_col = i, j
                break
        if crash_row != -1:
            break
    
    # 移動方向ごとの座標の変化量を定義
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    # 到達可能なマスを記録するための配列を初期化
    reachable = [[False] * W for _ in range(H)]
    reachable[crash_row][crash_col] = True

    # 移動をシミュレートして到達可能なマスを更新
    for move in T:
        dx, dy = moves[move]
        next_reachable = [[False] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if not reachable[i][j]:
                    continue
                ni, nj = i + dx, j + dy
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.':
                    next_reachable[ni][nj] = True
        reachable = next_reachable

    # 到達可能なマスの個数を数える
    count = sum(sum(row) for row in reachable)

    return count

# 入力を受け取る
H, W, N = map(int, input().split())
T = input()
S = [input().strip() for _ in range(H)]

# 不時着したマスを海に変更
for i in range(H):
    for j in range(W):
        if S[i][j] == 'X':
            S[i] = S[i][:j] + '.' + S[i][j+1:]
            break
    if S[i][j] == '.':
        break

# 結果を出力
print(count_possible_positions(H, W, N, T, S))
