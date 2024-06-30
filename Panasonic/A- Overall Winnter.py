n = int(input())
s = list(input())

t_count = 0
a_count = 0
for i in range(n):
    if s[i] == "T":
        t_count += 1
    else:
        a_count += 1

if t_count > a_count:
    print("T")
elif t_count < a_count:
    print("A")
else:
    for i in range(n):
        if s[i] == "T":
            t_count += 1
        else:
            a_count += 1
        if t_count > a_count:
            print("T")
            break
        elif t_count < a_count:
            print("A")
            break
