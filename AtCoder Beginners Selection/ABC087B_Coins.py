a=input()
b=input()
c=input()
x=input()

count = 0
for i in range(int(a)+1):
    for m in range(int(b)+1):
        for n in range(int(c)+1):
            total = 500*i + 100*m + 50*n
            if int(total) == int(x):
                count += 1
            elif int(total) > int(x):
                break

print(count)