def solve(n: int, a: list[int], w: list[int]) -> int:
    boxes = [[] for _ in range(n + 1)]
    for i in range(n):
        boxes[a[i]].append(w[i])
    box_weights = [sum(weights) for weights in boxes]

    move_cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            move_cost[i][j] = abs(box_weights[j] - box_weights[i])

    dp = [[float('inf')] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0

    for k in range(2, n + 1):
        for l in range(1, n + 1 - k + 1):
            i = l
            j = l + k - 1

            min_cost = float('inf')
            for m in range(i, j + 1):
                min_cost = min(min_cost, dp[i][m] + dp[m + 1][j] + move_cost[i][j])

            dp[i][j] = min_cost

    return dp[1][n]

n = int(input())
a = [int(input()) for _ in range(n)]
w = [int(input()) for _ in range(n)]

result = solve(n, a, w)

print(result)
