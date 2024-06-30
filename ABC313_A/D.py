def query(x):
    # 質問を行い、応答を受け取る
    print('?', ' '.join(map(str, x)))
    return int(input())

def main():
    # N と K を受け取る
    N, K = map(int, input().split())

    # A の要素を特定するための辞書を初期化
    elements = {}

    # 奇数のリストを作成
    odd_list = [i for i in range(1, N+1) if i % 2 == 1]

    # クエリの回数をカウント
    query_count = 0

    # N回以下の質問で A の内容を特定する
    for i in range(0, N, K):
        # 質問と応答を取得
        x = odd_list[i:i+K]
        response = query(x)

        # クエリの回数を更新
        query_count += 1

        # 応答によって A の要素を特定する
        for j in range(K):
            if i+j+1 not in elements:
                elements[i+j+1] = response

    # クエリの回数が N 未満の場合、残りの要素を特定する
    if query_count < N:
        for i in range(1, N+1):
            if i not in elements:
                response = query([i])
                # クエリの回数を更新
                query_count += 1
                elements[i] = response

    # A の要素を出力して終了
    print('!', ' '.join(map(str, [elements[i] for i in range(1, N+1)])), flush=True)

if __name__ == "__main__":
    main()

