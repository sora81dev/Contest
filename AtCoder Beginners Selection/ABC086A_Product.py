import math

a,b=map(int,input().split())
Volume=a*b

if Volume/2==math.floor(Volume/2):
    print("Even")
else:
    print("Odd")