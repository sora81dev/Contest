N = int(input())
S = []
for i in range(N):
    S.append(input())

S.sort(key=len)
print("".join(S))