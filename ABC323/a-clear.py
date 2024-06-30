S = input()
list=[]
for i in range(2, 17, 2):
    if S[i - 1] == '0':
        list.append(True)
    else:
        list.append(False)

if False in list:
    print("No")
else:
    print("Yes")