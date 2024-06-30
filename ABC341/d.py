N, M, K = input().split()

N_int = int(N)
M_int = int(M)
K_int = int(K)

NM_list = []

result=[]
for i in range(1, K_int+3):
    if (i%N_int == 0)^(i%M_int == 0):
        result.append(i)

print(result[K_int-1])