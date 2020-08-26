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