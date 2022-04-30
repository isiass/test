from re import M


def fac(num):
    """求阶乘"""
    result=1
    for n in range(1,num+1):
        result*=n
        # 返回num的阶乘(因变量)
        return result
    
m=int(input('m='))
n=int(input('n='))
# 调用函数
print(fac(m)//fac(n)//fac(m-n))