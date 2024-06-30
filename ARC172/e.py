def find_n(X):
    for n in range(1, 10**9+1):
        if n % 10**9 == X:
            return n
    return -1

# 入力
Q = int(input())
X_list = [int(input()) for _ in range(Q)]

# 出力
for X in X_list:
    print(find_n(X))
