import numpy as np
import random

# 简单应用
t = np.array([1,2,3])
print(t)
print(type(t)) # 类型
print(t.dtype) # 数据类型

# arange(start, stop, step, dtype)，根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。
print(np.arange(10))
print(np.arange(4,10,2)) # 4-10的数，步长为2

# 调整数据类型
flag = np.array([1,0,1,1,0],dtype=bool)
print(flag)
print(flag.astype("int8"))

#numpy中的小数
num = np.array([random.random() for i in range(10)])
print(num)
print(num.dtype)
print(np.round(num,2))



# shape 数组的形状维度，对于矩阵，n 行 m 列
t1 = np.arange(12)

print(t1)

print(t1.shape)

t2 = np.array([[1,2,3],[4,5,6]])

print(t2)

print(t2.shape)

t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(t3)

print(t3.shape)

t4 = np.arange(12)

print(t4)

# 3行4列
print(t4.reshape((3,4)))

t5 = np.arange(24)

# 2维数组，每组3行4列
print(t5.reshape((2,3,4)))

print(t5.reshape((4,6)))

# 不会对t5原数值改变
print(t5)

# 需要对t5数值发生改变可以作如下操作
t5 = t5.reshape((4,6))

print("t5:\n"+str(t5))

# 变回1维数组
print(t5.reshape((24,)))

print(t5.reshape((24,1)))

print(t5.reshape((1,24)))

# 假设t5不知道有多少个数，可通过以下方式得出。
t6 = t5.reshape((t5.shape[0]*t5.shape[1],))

# t5行数
print(t5.shape[0])
# t5列数
print(t5.shape[1])
# t5 行*列=总个数
print(t5.shape[0]*t5.shape[1])
print("\n")

# t6+2会对每一个数组元素都做加法
print(t6)
print(t6+2)
print("\n")
# t6/2会对每一个数组元素都做除法
print(t6)
print(t6/2)
print("\n")
# t6*2会对每一个数组元素都做乘法
print(t6)
print(t6*2)
print("\n")

# 数组相加，数组相同(行，列)的情况下数组元素一一对应相加
print(t5)
print("\n")
t7 = np.arange(100,124).reshape(4,6)
t7 = t5+t7
print(t7)
print("\n")

# 数组相减，数组相同(行，列)的情况下数组元素一一对应相减
print(t7)
t8 = np.arange(100,124).reshape(4,6)
print(t7-t8)

# 数组广播
w1 = np.arange(10)
print(w1.reshape((2,5)))
w2 = np.arange(20,30)
print(w2.reshape(2,5))
print(w1*w2)

