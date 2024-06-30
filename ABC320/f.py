import sys
input = sys.stdin.readline

X, N, H = map(int, input().split())
dp = [float('inf')] * (X + 1)
dp[0] = 0

for _ in range(N):
    P, F = map(int, input().split())
    for i in range(X, -1, -1):
        if dp[i] != float('inf'):
            for j in range(1, H + 1):
                if i + j > X:
                    break
                dp[min(X, i + F)] = min(dp[min(X, i + F)], dp[i] + P)

answer = dp[X]
if answer == float('inf'):
    print(-1)
else:
    print(answer)
