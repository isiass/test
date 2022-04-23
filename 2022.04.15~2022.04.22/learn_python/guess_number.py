# 猜数字
import random


answer=random.randint(1,100)
counter = 0
while True:
    counter+=1
    number=input("请输入你要猜的数:")
    if number<answer:
        print("猜小了")
    elif number<answer:
        print("猜大了")
    
    elif number==answer:
        print("你猜对了！")
        break
    else:
        print("猜的范围不对")
        continue
    
print(f"你一共猜了{counter}次")
    