N = input()                         #int
Q = list(map(int,input().split()))  #int (list)
A = list(map(int,input().split()))  #int (list)
B = list(map(int,input().split()))  #int (list)

A_Sp_N = []
B_Sp_N = []
B_Sp_N_i=[]
A_Sp_N_i = []
Q_excecct =[]

for i in range(int(N)):
    if int(A[i]) == 0:
        A_Sp_N_i.append(0)
    else:
        A_Sp_N_i.append(int(Q[i]/A[i]))
        A_Sp_N.append(int(Q[i]/A[i]))
A_min = min(A_Sp_N)
for i in range(int(N)):
    Q_excecct.append(int(Q[i]-A[i]*A_min))
for i in range(int(N)):
    if int(B[i]) == 0:
        B_Sp_N_i.append(0)
    else:
        B_Sp_N_i.append(int(Q_excecct[i]/B[i]))
        B_Sp_N.append(int(Q_excecct[i]/B[i]))

B_min = min(B_Sp_N)
print(B_min)
print(A_min)
print(B_Sp_N)
print(A_min+B_min)