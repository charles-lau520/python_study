import math

f1 = 20
f2 = 10

alpha = math.pi * 3

x_force = f1 + f2 * math.sin(alpha)
y_force = f2 * math.cos(alpha)

force = math.sqrt(x_force * x_force + y_force ** 2)

print('The result is: ',round(force,2),'N')

name = input("input your name:")
age = input("input your age:")

age = int(age)
age += 10

print("your name:"+name)
print("your age:"+str(age))

