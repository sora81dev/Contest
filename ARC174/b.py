def min_bribe_for_avg_reviews(A, P):
    total_reviews = sum(A)
    target_reviews = (3 * total_reviews) - 1
    bribe = 0
    i = 4
    while total_reviews < target_reviews:
        if A[i] == 0:
            i -= 1
            continue
        print("i:", i) # 追加
        bribe_needed = (target_reviews - total_reviews) // i
        bribe_cost = min(bribe_needed, A[i])
        bribe += bribe_cost * P[i]
        total_reviews += bribe_cost * i
        A[i] -= bribe_cost
    return bribe

# テストケース数を取得
T = int(input())

# 各テストケースについて処理
for _ in range(T):
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    print(min_bribe_for_avg_reviews(A, P))
