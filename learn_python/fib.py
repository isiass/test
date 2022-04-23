#实现打印斐波那契数列第n行，里面加入了一些错误处理，但还有待改进
# 写一个函数,求斐波那契数列的第n项(即F(N)). 用到了递归函数和循环的知识
import errno


def fib():  # 定义一个递归函数,
    n = int(input("请输入一个数："))

    try:
        if n == 0:
            return 0
        if n > 1:
            if n < 3:
                return 1
            fib1 = fib2 = 1  # 定义好前两项，为后面循环做铺垫
            for i in range(3, 100000):  # 从第三个数进行循环的次数
                fib1, fib2 = fib2, fib1 + fib2
                if n == i:
                    return fib2
        else:
            raise ValueError("必须是正整数！")
    except ValueError as e:
        print('except:', e)

    finally:
        print('finally')

    print("end")


if __name__ == "__main__":

    ww = fib()
    if ww == None:
        print("输入错误")
    else:
        print(ww)
