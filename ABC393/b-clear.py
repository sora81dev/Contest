S_i = str(input())
S = list(S_i)

count = 0
temp_A = 0
temp_B = 0

#print(len(S))

for i in range(len(S)):
    if S[i] == "A":
        temp_A = i
        #print(f"temp_A: {temp_A}")
        for j in range(i+1, len(S)):
            if S[j] == "B":
                temp_B = j
                #print(f"temp_B: {temp_B}")

                index = temp_B + (temp_B - temp_A)
                if index < len(S) and S[index] == "C":
                    count += 1
                    #print(f"find! count:{count} A {temp_A} B {temp_B}")

print(count)