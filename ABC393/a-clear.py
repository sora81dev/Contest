def kakicheck(s1, s2):
    if s1 == "fine" and s2 == "fine":
        return 4
    
    if s1 == "fine" and s2 == "sick":
        return 3
    
    if s1 == "sick" and s2 == "fine":
        return 2
    
    if s1 == "sick" and s2 == "sick":
        return 1


S = list(map(str, input().split()))

S1 = S[0]
S2 = S[1]

print(kakicheck(S1, S2))