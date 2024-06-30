N = input()
A = list(map(int, input().split()))
A.insert(0,0)
N_int = int(N)
add = 0

for i in range(N_int-1):
    if A[i] + A[i+1] == abs(A[i] + A[i+1]):
        pass
    else:
        add += abs(A[i]+A[i+1])

print(sum(A) + add)