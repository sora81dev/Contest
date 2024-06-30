# 入力の読み込み
N = int(input())
results = []
for i in range(N):
    A, B = map(int, input().split())
    success_rate = A / (A + B)
    results.append((success_rate, i + 1))

# 成功率の高い順に並び替える
results.sort(reverse=True)

# 結果の出力
output = [str(result[1]) for result in results]
print(" ".join(output))
