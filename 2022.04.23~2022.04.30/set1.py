#创建一个空集合
set1=set()
# 添加元素
set1.add(33)
set1.add(55)
set1.update({1,20,100,1000}) # update方法
print(set1)

#删除元素
set1.discard(20)
set1.discard(22)
print(set1)

# 指定元素
if 1 in set1:
    set1.remove(1)
print(set1)
# 随机删除元素并返回该元素
print(set1.pop())

# clear方法清空
set1.clear()
print(set1)