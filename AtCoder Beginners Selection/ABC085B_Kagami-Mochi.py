N=input()
list_d=[]
for i in range(int(N)):
    d=input()
    list_d.append(d)
list_d.sort()
list_d_set=set(list_d)
list_d_set_list=set(list_d_set)
print(len(list_d_set_list))