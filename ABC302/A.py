A,B=map(int,input().split())

# 敵の体力をBで割った商と余りを取得
quotient = A // B
remainder = A % B

# 攻撃回数の最小値は商 + 余りが0でなければ+1する
min_attacks = quotient + (1 if remainder > 0 else 0)

print(min_attacks)