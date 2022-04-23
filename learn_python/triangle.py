# 实现杨辉三角打印前numRows行，但仍需要改进。
numRows = int(input('numRows:'))
N = []
for i in range(numRows):
    N.append([])
    for j in range(0, i+1):
        if j == 0 or i == j:  # 杨辉三角特点：j=0和i=j时都等于1
            N[i].append(1)
        else:
            N[i].append(N[i-1][j-1]+N[i-1][j])


if __name__ == "__main__":
    print(N)
N.remove([1])