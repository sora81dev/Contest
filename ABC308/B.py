# 入力の読み込み
N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

# 料理の価格を格納する辞書を作成
price_dict = dict(zip(D, P))
price_dict["other"] = P[0]  # 異なる色の料理の価格

# 高橋くんが食べた料理の価格の合計を求める
total_price = 0
for dish in C:
    if dish in price_dict:
        total_price += price_dict[dish]
    else:
        total_price += price_dict["other"]

# 合計価格の出力
print(total_price)
