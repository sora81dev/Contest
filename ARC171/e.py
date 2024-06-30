import sys

MOD = 998244353

def main():
    # 入力
    N, M, A, B = map(int, sys.stdin.readline().split())
    N_int = int(N)
    M_int = int(M)
    A_int = int(A)
    B_int = int(B)
    # dp[i][j][k]: i行目まで白石を配置し、j個の白石を配置し、
    # 黒石が(k, A)にいるときの配置の個数
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][A_int] = 1

    # 各行について処理
    for i in range(1, N + 1):
        # 各白石の個数について処理
        for j in range(M + 1):
            # 各列について処理
            for k in range(N + 1):
                # 白石を置かない場合
                dp[i][j][k] += dp[i - 1][j][k]

                # 白石を置く場合
                if j < M:
                    # 行方向に白石を置く
                    if i > 1 and k > 1:
                        dp[i][j + 1][k - 1] += dp[i - 1][j][k]
                    # 列方向に白石を置く
                    if k > 1:
                        dp[i][j + 1][k] += dp[i - 1][j][k]

    # 出力
    print(dp[N][M][B] % MOD)

if __name__ == "__main__":
    main()
