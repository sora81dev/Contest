def order_people(n, a):
    order = [0] * n

    for i in range(n):
        if a[i] == -1:
            order[0] = i + 1
        elif order[i] == 0:
            j = i
            while order[j] == 0:
                order[j] = i + 1
                j = a[j] - 1

    return order


# 標準入力からNと数列Aを取得
n = int(input())
a = list(map(int, input().split()))

# 人々の順番を計算
result = order_people(n, a)

# 結果を出力
print(*result)
