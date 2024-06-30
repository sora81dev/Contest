# プレイヤーの情報を辞書に格納
player_ratings = {
    "tourist": 3858,
    "ksun48": 3679,
    "Benq": 3658,
    "Um_nik": 3648,
    "apiad": 3638,
    "Stonefeang": 3630,
    "ecnerwala": 3613,
    "mnbvmar": 3555,
    "newbiedmy": 3516,
    "semiexp": 3481
}

# 入力としてハンドルネームを受け取る
S = input().strip()

# ハンドルネームに対応するレーティングを出力
if S in player_ratings:
    print(player_ratings[S])
else:
    # ハンドルネームが見つからない場合のエラーメッセージ
    print("該当するプレイヤーが見つかりません。")
