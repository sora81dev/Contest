import sys

def calc():
    N = int(input())
    S = list(str(input()))

    ones = [i for i in range(N) if S[i] == '1']

    k = len(ones)

    if k == 1:
        print(0)
        return
    
    index = k // 2
    pos = ones[index]

    moves = sum(abs(ones[i] - (pos - index + i)) for i in range(k))

    # 結果を出力
    print(moves)

calc()
