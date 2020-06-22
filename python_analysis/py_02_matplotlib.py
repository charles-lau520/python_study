# 导入包
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# 设置字体方式一：
# windows和linux设置字体的方式，mac不支持，会出现不能正常显示的效果
# font = {'family' : 'MicroSoft YaHei','weight' : 'bold','size' : 'larger'}
# matplotlib.rc("font",**font)

#设置字体方式二：  可以彻底解决上面设置字体可能出现不正常显示的问题
my_font = font_manager.FontProperties(fname="../myfont/msyh.ttf")

plt.figure(figsize=(20,8),dpi=80)

x = range(0,120)

y = [random.randint(20,35) for i in range(120)]

plt.plot(x,y)

#调整X轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]

_xtick_labels += ["11点{}分".format(i) for i in range(60)]

# 取步长，数字和字符串一一对应，数据的长度一样
# rotation旋转的度数
#fontproperties用来设置表的中文正常显示
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间",fontproperties=my_font)

plt.ylabel("温度(摄氏度)",fontproperties=my_font)

plt.title("10点到12点每分钟气温的变化情况",fontproperties=my_font)

plt.show()






