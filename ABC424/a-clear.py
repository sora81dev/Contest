a, b, c = map(int, input().split())

def check():
    global a, b, c 

    if(a==b):
        return "Yes"
    
    if(a==c):
        return "Yes"
    
    if(b==c):
        return "Yes"
    
    return "No"

print(check())