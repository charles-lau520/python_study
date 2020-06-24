#绘制横着的条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ['战狼2','速度与激情8','功夫瑜伽','西游伏妖篇','变形金刚5：最后的勇士','摔跤吧！爸爸',
     '加勒比海盗5：死无对证','金刚：骷髅岛','极限特工：终极回归','生化危机6：终章','乘风破浪',
     '神偷奶爸3','智取威虎山','大闹天竺','金刚狼3：殊死一战','蜘蛛侠：英雄归来','悟空传','银河护卫队2','情圣','新木乃伊']

b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

# 设置字体
my_font = font_manager.FontProperties(fname="../myfont/msyh.ttf")

# 设置图形大小
plt.figure(figsize=(20,15),dpi=80)

# 绘制条形图
plt.barh(range(len(a)),b,height=0.3,color="orange")

plt.yticks(range(len(a)),a,fontproperties=my_font)

plt.grid(alpha=3)


# 添加描述信息
plt.xlabel("票房",fontproperties=my_font)
plt.ylabel("电影",fontproperties=my_font)
plt.title("票房对比图",fontproperties=my_font)

#plt.savefig("./bar.png")

plt.show()

