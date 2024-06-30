N = int(input())

poison_sum = 0  # 毒入り料理の美味しさの総和
treatment_sum = 0  # 解毒剤入り料理の美味しさの総和
poison_list = []  # 毒入り料理の美味しさを格納するリスト
for _ in range(N):
    X, Y = map(int, input().split())
    if X == 0:
        treatment_sum += Y
    else:
        poison_sum += Y
        poison_list.append(Y)

# 選択肢:
# 1. 毒入り料理をすべて食べる
# 2. 解毒剤入り料理と毒入り料理の中で最大のものを食べる
# 3. 解毒剤入り料理だけを食べる
# 4. 解毒剤入り料理と毒入り料理の中で2番目に美味しいものを食べる

option1 = treatment_sum + poison_sum  # 毒入り料理をすべて食べる場合
option2 = treatment_sum + max(poison_list)  # 解毒剤入り料理と最大の毒入り料理を食べる場合
option3 = treatment_sum  # 解毒剤入り料理だけを食べる場合
option4 = treatment_sum + max(poison_list) if len(poison_list) >= 2 else float('-inf')  # 解毒剤入り料理と2番目に美味しい毒入り料理を食べる場合

result = max(option1, option2, option3, option4)
print(result)
