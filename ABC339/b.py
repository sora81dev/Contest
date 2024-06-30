H, W, N = input().split()
#print(f"H:{H}, W:{W}, N:{N}")
list = [["."]*int(W) for i in range(int(H))]

# 変数
T_look = 0
T_pos_x = 0
T_pos_y = 0
for i in range(int(N)):
    # 現在いるマスが白で塗られているなら
    if list[T_pos_y][T_pos_x] == ".":

        #黒に塗り替える
        list[T_pos_y][T_pos_x] = "#"

        #時計回りに90度回転
        T_look += 90
        if T_look == 360:
            T_look = 0

        #向いてる方向を確認し、移動する
        if T_look == 0:
            T_pos_y -= 1
            if T_pos_y == -1:
                T_pos_y =0
        if T_look == 90:
            T_pos_x += 1
            if T_pos_x == int(W):
                T_pos_x = 0
        if T_look == 180:
            T_pos_y += 1
            if T_pos_x == int(H):
                T_pos_y =0
        if T_look == 270:
            T_pos_x -= 1
            if T_pos_x == -1:
                T_pos_x = 0

    else:
    
        #白に塗り替える
        list[T_pos_y][T_pos_x] = "."

        #反時計回りに90度回転
        T_look -= 90
        if T_look == -90:
            T_look = 270
    
        #向いている方向を確認し、移動
        if T_look == 0:
            T_pos_y -= 1
            if T_pos_y == -1:
                T_pos_y =0
        if T_look == 90:
            T_pos_x += 1
            if T_pos_x == int(W):
                T_pos_x = 0
        if T_look == 180:
            T_pos_y += 1
            if T_pos_x == int(H):
                T_pos_y =0
        if T_look == 270:
            T_pos_x -= 1
            if T_pos_x == -1:
                T_pos_x = 0

test = []

for i in range(int(W)-1):
    test.append("".join(list[i]))
for i in range(int(W)-1):
    print(test[i])