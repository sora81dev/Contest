def max_currency(N, A, ST):
    # 各国の通貨を保持するリスト
    currencies = [A[0]]

    # 各国の通貨の最大値を計算
    for i in range(N-1):
        Si, Ti = ST[i]
        currencies.append(min(Ti, currencies[-1] - Si + Si // Ti * Ti))

    return currencies[-1]

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
ST = [list(map(int, input().split())) for _ in range(N-1)]

# 答えを出力
print(max_currency(N, A, ST))
