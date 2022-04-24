# 嵌套的字典
from multiprocessing.sharedctypes import Value
from unicodedata import name


students={
    1001:{'name':'狄仁杰','sex':'True','age':'22','place':'山西大同'},
    1002:{'name':'白元芳','sex':'True','age':'23','place':'河北保定'},
    1003:{'name':'武则天','sex':'False','age':'20','place':'四川广元'}
}
# get方法通过键来获取对应的值，如果取不到不会引发Keyerror异常而是返回None或设定的默认值
print(students.get(1001))
print(students.get(1005)) # None
print(students.get(1005,{'name':'无名氏'}))

# 获取键
print(students.keys())
# 获取值
print(students.values())
# 获取键值对
print(students.items())
# 对所有键值对循环遍历
for key,value in students.items():
    print(key,'--->',value)
# 利用pop方法通过键删除对应键值并返回
stu1=students.pop(1002)
print(stu1)
print(len(students))
stu2=students.pop(1005)
print(stu2)