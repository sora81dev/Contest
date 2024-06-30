def max_sum_after_operation(N, C, A):
    max_sum = float('-inf')
    max_range = None
    current_sum = 0
    for i in range(N):
        if current_sum * C > max_sum:
            max_sum = current_sum * C
            max_range = (i - len(current_range), i - 1)
        if current_sum + A[i] < 0:
            current_sum = 0
            current_range = []
        else:
            current_sum += A[i]
            current_range.append(A[i])

    if current_sum * C > max_sum:
        max_sum = current_sum * C
        max_range = (N - len(current_range), N - 1)

    for i in range(max_range[0], max_range[1] + 1):
        A[i] *= C

    total_sum = sum(A)

    return total_sum

# 入力を受け取る
N, C = map(int, input().split())
A = list(map(int, input().split()))

# 結果を出力する
print(max_sum_after_operation(N, C, A))
