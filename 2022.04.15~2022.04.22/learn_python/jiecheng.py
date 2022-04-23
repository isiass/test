# 求数的阶乘
# 学到的东西: 可以先把头和尾想好,然后一步步补充缺失东西

def get_jiecheng(number):  # 定义函数
    result = 1  # 初始化为1
    while number > 0:
        result *= number  # 一直乘number
        number -= 1  # number每次减1,减到1停止
    return result


print("jiecheng =", get_jiecheng())  # 输入参数可求阶乘