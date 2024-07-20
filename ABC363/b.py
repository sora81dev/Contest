N, T, P = input().split()
N_i, T_i, P_i = int(N), int(T), int(P)

L = list(map(int, input().split()))

def main(N, T, P, L):
    count = 0
    day = 0


    for i in range(len(L)):
        if L[i] >= T:
            count += 1

        if count == P:
            return 0
        
    count = 0

    while 1:
        day += 1
        count = 0
        for i in range(len(L)):
            L[i] = L[i] + 1

        for i in range(len(L)):
            if L[i] >= T:
                count += 1

            if count == P:
                return day



result = main(N_i, T_i, P_i, L)
if result == None:
    print(0)

else:
    print(result)