# B - Make Target

N = int(input())
list = [["." for j in range(N)] for i in range(N)]

def make_target():
    global N, list

    list_c = list

    for i in range(1, N+1):
        j = N + 1 - i

        if i <= j:
            if i%2 == 0:
                place_c = "."
            else:
                place_c = "#"

            for k in range(i-1, j):
                for l in range(i-1, j):
                    list_c[k][l] = place_c
    
    return list_c

list_c2 = make_target()

for i in range(N):
    temp = "".join(list_c2[i])
    print(temp)