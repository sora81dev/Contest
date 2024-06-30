def is_extended_abc_string(s):
    """
    文字列 s が拡張 ABC 文字列かどうかを判定する。

    Args:
      s: 判定する文字列

    Returns:
      s が拡張 ABC 文字列であれば True、そうでなければ False
    """

    s_list = []
    for c in s:
        s_list.append(c)

    # 簡略化

    while len(s_list) > 2:
        if s_list[0] == s_list[1]:
            s_list = s_list[1:]
        elif ord(s_list[0]) + 1 == ord(s_list[1]):  # 文字列を文字コードに変換
            s_list[0] = s_list[0] * 2
            s_list = s_list[1:]
        else:
            return False

    # 判定

    if len(s_list) == 2:
        return s_list[0] == s_list[1]
    elif len(s_list) == 1:
        return True
    else:
        return False


def main():
    s = input()
    print("Yes" if is_extended_abc_string(s) else "No")


if __name__ == "__main__":
    main()
