from matplotlib import pyplot as plt

# 设置图片大小
# figure 图形图标的意思，在这里指的就是我们画的图
# 通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
# 在图像模糊的时候可以传入dpi参数，让图片更加清晰
plt.figure(figsize=(6.4,4.8),dpi=80)

#设置横轴和纵轴的数值
x = range(2,26,2)
y = [25,10,24,25,30,20,30,32,30,31,33,35]

# 绘图
plt.plot(x,y)

#设置X轴的刻度
#plt.xticks(x)
plt.xticks(range(2,25))
plt.yticks(range(min(y),max(y)+1))
#_xtick_labels = [i/2 for i in range(4,49)]
#plt.xticks(_xtick_labels)

#保存
#plt.savefig("./t1.png")

#展示图形
plt.show()


