def main():
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # A の最大値と最小値の差を求める
    max_val = max(A)
    min_val = min(A)
    diff = max_val - min_val

    # 操作回数を計算する
    if diff <= 1:
        ans = 0
    else:
        ans = diff - 1

    # 答えを出力する
    print(ans)

if __name__ == "__main__":
    main()
