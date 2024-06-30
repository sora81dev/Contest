def solve(N, edges):
    # 各頂点から各頂点へのパス上の辺の数を数える

    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(N):
                    if i != k and j != k:
                        if edges[k][0] == i and edges[k][1] == j:
                            dp[i][j] += 1

    # 頂点 u について f(u) の値を求める

    answer = []
    for i in range(N):
        for j in range(i + 1, N):
            answer.append(dp[i][j] + dp[j][i])

    return answer


def main():
    # 入力を受け取る

    N = int(input())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))

    # 問題を解く

    answer = solve(N, edges)

    # 出力する

    print(*answer)


if __name__ == "__main__":
    main()
