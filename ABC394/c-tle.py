def check(s):
    while "WA" in s:
        s = s.replace("WA", "AC", 1)

S = input()
print(check(S))
