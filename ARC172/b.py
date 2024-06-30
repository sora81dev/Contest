def main():
    N, K, L = map(int, input().split())

    # 組み合わせの数 N_C_K を計算
    n_factorial = 1
    for i in range(1, N + 1):
        n_factorial *= i

    k_factorial = 1
    for i in range(1, K + 1):
        k_factorial *= i

    nk_factorial = 1
    for i in range(1, N - K + 1):
        nk_factorial *= i

    # 選んだ K 文字すべてが異なる場合の数を求める
    answer = n_factorial // (k_factorial * nk_factorial) * L
    for i in range(1, K + 1):
        
        answer *= L - i

    # 998244353 で割った余りを求める
    answer %= 998244353

    print(answer)

if __name__ == "__main__":
    main()
