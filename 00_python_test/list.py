lst = [1,2,3]
print(lst)

lst[1] = 200
print(lst)

lst.append(300)
print(lst)

lst.insert(0,10)
print(lst)

lst.insert(3,20)
print(lst)

lst2 = ['a','b']
lst.extend(lst2)
print(lst)

lst.extend("book")
print(lst)

lst.pop(0)
print(lst)

lst.remove('b')
print(lst)

lst2 = [2,23,1,4,5,34,23]
lst2.sort(reverse=False)
print(lst2)

lst2.reverse()
print(lst2)

# 将字符串转换为列表
str = "python"
lst3 = list(str)
print(lst3)

# 列表连接成字符串
str = "".join(lst3)
print(str)





