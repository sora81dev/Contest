N, M = map(int, input().split())
players = []

for i in range(N):
    A = list(map(str, input().split()))
    S = input().strip()
    score = sum(int([A[j] for j in range(M) if S[j] == 'o']))
    solved_count = S.count('o')
    players.append((score, solved_count, i + 1))

players.sort(key=lambda x: (-x[0], x[1], x[2]))

answers = []
for i in range(N):
    current_player = players[i]
    max_possible_score = current_player[0] + (M - current_player[1]) * 100
    can_win = True
    for j in range(i + 1, N):
        if max_possible_score <= players[j][0]:
            can_win = False
            break
    if can_win:
        answers.append("Yes")
    else:
        answers.append("No")

for ans in answers:
    print(ans)
