lst = (1,2,3,"python","love",[12,43,56])
print(lst)
# 将元组改为列表，就可以对列表内容进行修改
lst2 = list(lst)
print(lst2)
lst2[2] = 300
print(lst2)

lst = tuple(lst2)
print(lst)

# 切片
lst3 = lst[::2]
print(lst3)

lst3 = list(lst[5::1])
print(lst3[0])



