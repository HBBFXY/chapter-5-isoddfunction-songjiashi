def isOdd(param):
    # 判断参数是否为整数类型
    if isinstance(param, int):
        # 若为整数，判断是否为奇数（奇数对 2 取余结果为 1）
        return param % 2 == 1
    else:
        # 若不是整数，直接返回 False
        return False
