def win_probability(N, L, D):
    # あなたのサイコロを振る目の期待値
    your_expected_value = (D + 1) / 2
    
    # ディーラーのサイコロを振る目の期待値
    dealer_expected_value = (D + 1) / 2
    
    # 勝率を計算
    if your_expected_value <= N:
        return 1.0
    elif dealer_expected_value >= L or your_expected_value > N:
        return 1.0
    else:
        return (N - your_expected_value + 1) / N

# 入力を受け取る
N, L, D = map(int, input().split())

# 勝率を計算して出力
print(win_probability(N, L, D))
