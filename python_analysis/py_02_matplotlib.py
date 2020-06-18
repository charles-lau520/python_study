from matplotlib import pyplot as plt
import random

plt.figure(figsize=(20,8),dpi=80)

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.plot(x,y)
#调整X轴的刻度
_xtick_labels = ["10:{}".format(i) for i in range(60)]
_xtick_labels += ["11:{}".format(i) for i in range(60)]

# 取步长，数字和字符串一一对应，数据的长度一样
# rotation旋转的度数
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)

plt.show()



