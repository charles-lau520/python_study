#开发人员  :  
#_+_coding:  UTF-8_*_
#开发团队  :  LC_Group
#开发人员  :  
#开发时间  :  2020/8/24 16:21
#文件名称  :  string.py
#开发工具  :  PyCharm

a = "I LOVE PYTHON"
list = a.split()
print(list)
new_a = "-".join(list)
print(new_a)

b = "I LIKE {0} AND {1}".format("APPLE","ORANGE")
print(b)
# 占位符长度
# {0:10} 10个占位符
# {1:>15} 15个占位符并右对齐
b = "I LIKE {0:10} AND {1:^10} AND {2:>15}".format("APPLE","BANANA","ORANGE")
print(b)
c = "she is {0:4d} year old and {1:.1f}m hight".format(20,1.68)
print(c)



