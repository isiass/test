set1={1,2,3,4,5,6,7}
set2={2,4,6,8,10}
# 交集
print(set1 & set2)
print(set1.intersection(set2))
# 并集
print(set1 | set2)
print(set1.union(set2))
# 差集
print(set1-set2)
print(set1.difference(set2))
#对称差相当于两个集合的并集减去交集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
print((set1|set2)-(set1&set2))
