N = int(input())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

skill = []

num_arr = list(range(1, N+1))

A_pop = A[:]
B_pop = B[:]
num_arr_pop = num_arr[:]


for i in range(len(A)):
    if A_pop[i] == 200001:
        continue

    if A[i] == 0 and B[i] == 0:
        skill.append(i+1)
        A_pop[i] = 200001
        B_pop[i] = 200001
        num_arr_pop[i] = 200001

get_skill_pe = 200001
force = True


if (len(A_pop) != 0):
    while get_skill_pe != 0 or get_skill_pe == 200001 or force:
        get_skill_pe = 0
        force = False

        for i in range(len(A_pop)):
            if A_pop[i] == 200001:
                continue

            if A_pop[i] in skill or B_pop[i] in skill:
                skill.append(num_arr_pop[i])
                A_pop[i] = 200001
                B_pop[i] = 200001
                num_arr_pop[i] = 200001

                get_skill_pe += 1


print(len(skill))