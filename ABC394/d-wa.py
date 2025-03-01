S = list(input())

def check(s):
    stack = []
    search = {")": "(", "]": "[", ">": "<"}

    for i in s:
        if i in "(<[":
            stack.append(i)
        
        elif i in ">)]":
            if not stack or stack [-1] != search[i]:
                return False
            
            stack.pop()
        
    return len(stack) == 0


print(check(S))