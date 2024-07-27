N = int(input())
S = []
for _ in range(N):
    S.append(str(input()))


def main(N, S):
    for i in range(N):
        if not i == 0:
            if(S[i-1] == S[i] == "sweet"):
                if not i == len(S)-1:
                    return "No"

    return "Yes"

print(main(N, S))