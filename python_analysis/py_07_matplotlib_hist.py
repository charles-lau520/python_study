from matplotlib import pyplot as plt
from matplotlib import font_manager

a = [121,98,115,124,167,154,124,176,146,118,129,109,119,128,113,156,124,120,138,134,176,178,182,165,146,172]

# 计算组数
d = 5 #组距
num_bins = (max(a) - min(a))//d

plt.figure(figsize=(20,8),dpi=80)
plt.hist(a,20)

plt.xticks(range(min(a),max(a)+d,d))

plt.grid()

plt.show()

