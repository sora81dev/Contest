A, B, C, D = input().split()

def check_report(A, B, C, D):
    if A*60 + B <= C*60 + D:
        return "No"
    
    else:
        return "Yes"
        
print(check_report(A, B, C, D))