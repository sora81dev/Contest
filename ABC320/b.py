def longest_palindrome(S):
    n = len(S)
    dp = [[0] * 26 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(26):
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][S[i - 1] - ord('a') + 1] + 1)
    return max(dp[n])

S = input()
print(longest_palindrome(S))
