print(WindowsError)
x = 0
y = 0

while N % 2 == 0:
    x += 1
    N //= 2


if N == 1:
    print("Yes")
else:
    print("No")