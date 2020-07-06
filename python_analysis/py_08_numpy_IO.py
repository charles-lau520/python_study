import numpy as np
import random

gb_file_path = "./csv/test.csv"

t1 = np.loadtxt(gb_file_path,delimiter=",",dtype="int")

# print(t1)
# print("*"*100)
# 取1行
# print(t1[2])

# 取多行
# print("*"*100)
# print(t1[2:])

# 取不连续的多行
# print("*"*100)
# print(t1[[2,8,10]])

# 取列
# print("*"*100)
# print(t1[1,:])

# 取多行和多列，取第3行，第四列的值
# a = t1[2,3]
# print(a)

# 取多行和多列，取第3行到第五行，第2列到第四列的结果
# b = t1[2:5,1:4]
# print(b)

t = np.arange(24)
print(t)
tt = t.reshape((4,6))
# print(tt)
# print(tt<10)
# print(tt>10)
# tt[tt<10]=3
# print(tt)
# tt[tt>=10]=4
# print(tt)

# where条件，当tt>=10满足的话变为100，否则变为200
print(np.where(tt>=10,100,200))

# clip裁减,小于6的变为6，大于8的变为8
ttt = tt.clip(6,8)
print(ttt)

