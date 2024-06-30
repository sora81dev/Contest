def calculate_sum_greater_than_elements(arr):
    n = len(arr)
    result = []

    # 各要素について処理
    for i in range(n):
        current_element = arr[i]
        current_sum = 0

        # A[i] より大きな要素の和を計算
        for j in range(i + 1, n):
            if arr[j] > current_element:
                current_sum += arr[j]

        result.append(current_sum)

    return result


# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 各要素に対する問題の答えを計算
result = calculate_sum_greater_than_elements(A)

# 結果を出力
print(*result)
