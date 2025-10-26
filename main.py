def isOdd(x):
    """
    判断输入是否为奇数
    
    参数:
    x: 任意类型的输入
    
    返回:
    bool: 只有当输入是整数且为奇数时返回True，其他情况返回False
    """
    # 首先检查类型是否为整数
    if not isinstance(x, int):
        return False
    
    # 然后检查是否为奇数（使用模运算）
    if x % 2 == 1:
        return True
    else:
        return False


# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_cases = [
        1,      # 正奇数 -> True
        3,      # 正奇数 -> True
        -1,     # 负奇数 -> True
        -3,     # 负奇数 -> True
        2,      # 正偶数 -> False
        0,      # 零 -> False
        -2,     # 负偶数 -> False
        3.14,   # 浮点数 -> False
        "5",    # 字符串 -> False
        True,   # 布尔值 -> False
        False,  # 布尔值 -> False
        [1],    # 列表 -> False
        None    # None -> False
    ]
    
    print("测试结果:")
    for case in test_cases:
        result = isOdd(case)
        print(f"isOdd({repr(case)}) = {result}")
    
    # 详细解释
    print("\n函数逻辑说明:")
    print("1. 首先检查输入的类型是否为整数 (isinstance(x, int))")
    print("2. 如果不是整数，立即返回 False")
    print("3. 如果是整数，检查是否能被2整除余1 (x % 2 == 1)")
    print("4. 如果余数为1，返回 True；否则返回 False")
