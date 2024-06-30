def check_sequence(nums):
    # 条件1: 数列が広義単調増加かどうかをチェック
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return "No"

    # 条件2: 数列の要素が100以上675以下かどうかをチェック
    for num in nums:
        if num < 100 or num > 675:
            return "No"

    # 条件3: 数列の要素が25の倍数かどうかをチェック
    for num in nums:
        if num % 25 != 0:
            return "No"

    return "Yes"

# 入力の読み込み
nums = list(map(int, input().split()))

# 判定結果の出力
print(check_sequence(nums))
