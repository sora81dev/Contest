def count_vote_sequences(N, votes):
    count_A = 0  # A 候補の獲得票数
    count_B = 0  # B 候補の獲得票数
    result = 1   # 開票結果の列としてあり得るものの数

    for i in range(1, N):
        if votes[i - 1] == 'A':
            count_A += 1
        else:
            count_B += 1

        # A 候補と B 候補の獲得票数が同数になる場合
        if count_A == count_B:
            result += 1

    return result

# 入力
N = int(input())
votes = input().split()

# 出力
print(count_vote_sequences(N, votes))
