# 入力を受け取る
N, M = map(int, input().split())
L = list(map(int, input().split()))

# 最大の単語幅を求める
max_word_width = max(L)

# 二分探索を用いて最小のウィンドウ幅を求める
left, right = max_word_width, sum(L)
while left < right:
    mid = (left + right) // 2  # ウィンドウの横幅の候補
    lines = 1  # 現在の行数
    current_width = 0  # 現在の行の横幅
    for word_width in L:
        if current_width + word_width <= mid:
            current_width += word_width
        else:
            lines += 1
            current_width = word_width
    if lines <= M:
        right = mid
    else:
        left = mid + 1

# 結果を出力
print(left)
