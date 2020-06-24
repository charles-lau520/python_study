#绘制横着的条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ["猩球崛起3:终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]

b_16 = [15746,312,4497,319]

b_15 = [12357,156,2045,168]

b_14 = [2358,399,2358,362]

bar_width = 0.1

x_14 = list(range(len(a)))

x_15 = [i+bar_width for i in x_14]

x_16 = [i+bar_width*2 for i in x_14]

# 设置字体
my_font = font_manager.FontProperties(fname="../myfont/msyh.ttf")

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)
print(range(len(a)))
# 绘制条形图
plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")

plt.bar(x_15,b_15,width=bar_width,label="9月15日")

plt.bar(x_16,b_16,width=bar_width,label="9月16日")

plt.grid(alpha=3)

plt.xticks(x_15,a,fontproperties=my_font)

plt.legend(prop=my_font)

# 添加描述信息
# plt.xlabel("票房",fontproperties=my_font)
# plt.ylabel("电影",fontproperties=my_font)
# plt.title("票房对比图",fontproperties=my_font)

#plt.savefig("./bar.png")

plt.show()

