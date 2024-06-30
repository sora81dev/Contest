N = int(input())
A = list(map(int, input().split()))

# f(i)の値と対応する添字を格納する辞書を作成
f = {}
for i in range(1, N + 1):
    f[i] = []

# Aの中でiが現れる添字をf(i)に追加
for j in range(len(A)):
    i = A[j]
    f[i].append(j + 1)

# f(i)の昇順にiを並べ替える
sorted_i = sorted(f, key=lambda x: f[x][1])

# 結果を出力
result = ' '.join(map(str, sorted_i))
print(result)
