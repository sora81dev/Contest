A=int(input())

def check():
    global A
    if 400%A == 0:
        return 400/A
    else:
        return -1
    
print(int(check()))