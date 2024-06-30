T = input()
T_int = int(T)

CASE = []
N = []
A = []
B = []

for i in range(T_int):
    temp = list(map(int,input().split()))
    CASE.insert(len(CASE), temp)

for i in range(len(CASE)):
    N.insert(len(N), CASE[i][0])
    A.insert(len(A), CASE[i][1])
    B.insert(len(A), CASE[i][3])

for i in range(len(CASE)):
    list = [[0 for i in range(N[i])] for j in range(N[i])]

#THIS FILE IS NOT COMPLETE