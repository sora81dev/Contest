S_list = list(str(input()))
flag = 0

def test():
    global S_list, flag
    for i in range(3):
        if S_list[i] == "R" and flag == 0:
            flag = 1
        if S_list[i] == "M" and flag == 1:
            flag = 2
        elif S_list[i] == "M" and flag == 0:
            return "No"
    
    return("Yes")

print(test())