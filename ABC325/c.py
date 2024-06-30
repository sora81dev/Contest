# Input
WaH = list(map(int, input().split()))

# Reset
list1 = [[0] * WaH[1]] * WaH[0]
Map_Temp = [] * WaH[0]
Map_Temp2 = [""] * WaH[0]
Map = [[0] * WaH[1]] * WaH[0]

# Input 2
for i in range(WaH[0]):
    Map_Temp.append(input(str))

# Break it down letter by letter and put it in List Map_Temp2.
for i in range(WaH[0]):
    Map_Temp2[i] = list(Map_Temp[i])

# Sharp to 1, dot to 0
for i in range(WaH[0]):
    for n in range(WaH[1]):
        print(f"REPORT {i*10+n}  i:{i} n:{n} list data[MAP_TEMP2] : {Map_Temp2[i][n]}")
        if Map_Temp2[i][n] == "#":
            Map[i][n] = 1
        else:
            Map[i][n] = 0

print(Map_Temp)
print(Map_Temp2)
print(Map)
print(Map_Temp2[0][0])
