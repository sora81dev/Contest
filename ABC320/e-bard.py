import bisect

N, M = map(int, input().split())

# 各人が得るそうめんの量と次に列に戻る時刻を保持するリストを初期化
soy_amounts = [0] * N
next_return_time = [0] * N

# イベント情報を処理
for _ in range(M):
    T, W, S = map(int, input().split())

    # リストをソートする
    next_return_time.sort()

    # 二分探索で、時刻 T に列にいる人を探す
    i = bisect.bisect_left(next_return_time, T)

    # 見つかったら、そうめんを配る
    if i < N and next_return_time[i] <= T:
        soy_amounts[i] += W
        next_return_time[i] = T + S

# 各人の得たそうめんの量を出力
for amount in soy_amounts:
    print(amount)
