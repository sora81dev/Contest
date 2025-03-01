# C - Shortest Duplicate Subarray

N = int(input())
A = list(map(str, input().split()))

def check():
    global N, A

    new_A = A

    for i in range(N):
        if len(set(new_A)) == len(new_A):
            if not i == 0:
                return i+1
            else:
                return -1
        
        new_A = []

        for j in range(0, i-1):
            new_A.append(A[j])

print(check())