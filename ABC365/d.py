N = int(input())
S = str(input())

def max_wins(N, S):

    takahashi_hands = []
    
    for i in range(N):
        if S[i] == 'R':

            takahashi_hands.append('P')
        elif S[i] == 'P':

            takahashi_hands.append('S')
        else:

            takahashi_hands.append('R')

    for i in range(1, N):
        if takahashi_hands[i] == takahashi_hands[i-1]:
            if takahashi_hands[i] == 'P':
                takahashi_hands[i] = 'R'
            elif takahashi_hands[i] == 'S':
                takahashi_hands[i] = 'P'
            else:
                takahashi_hands[i] = 'S'
    
    wins = 0
    for i in range(N):
        if (takahashi_hands[i] == 'P' and S[i] == 'R') or (takahashi_hands[i] == 'S' and S[i] == 'P') or (takahashi_hands[i] == 'R' and S[i] == 'S'):
            wins += 1
    
    return wins

print(max_wins(N, S))
