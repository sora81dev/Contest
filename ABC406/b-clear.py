N, K = input().split()
A = list(map(int, input().split()))

def calc(K, A):
    num = 1
    for i in range(len(A)):
        calculated = num * A[i]

        if int(len(str(calculated))) > int(K):
            num = 1

        else:
            num = calculated

    return num

print(calc(K, A))