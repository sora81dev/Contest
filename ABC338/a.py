S = list(input())

cnt = 0
for i in range(len(S)):
    if i==0 and S[i] == S[i].upper():
        pass
    elif i==0 and S[i] == S[i].lower():
        cnt+=1
    elif i<=1:
        if S[i] == S[i].lower():
            pass
        else:
            cnt+=1

if cnt >= 1:
    print("No")
else:
    print("Yes")