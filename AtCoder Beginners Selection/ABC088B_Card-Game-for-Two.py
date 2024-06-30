import math

N=input()
a=input()
alice=0
bob=0
list_a_change=[]
list_a=a.split()
for i in range(len(list_a)):
    list_a_change.append(int(list_a[i]))
list_a_change.sort(reverse=True)
alice=sum(list_a_change[::2])
bob=sum(list_a_change[1::2])
print(alice-bob)