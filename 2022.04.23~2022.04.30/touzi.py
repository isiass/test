#随机掷色子6000次，1到6点分别出现的次数
import random # 引入随机数

counters=[0] * 6   # counters=[0,0,0,0,0,0]
for _ in range(6000):
    face=random.randint(1,6)  # 点数在1到6随机
    counters[face-1]+=1  # 
for face in range(1,7):
    print(f'{face}一共出现了{counters[face-1]}次') # f-string 形式