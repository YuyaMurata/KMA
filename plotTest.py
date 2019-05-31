import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []
size = []
scale = 2

for i in range(0,10):
    x.append(i)
    y.append(5)
    size.append(i**scale)

plt.scatter(x, y, s=size)
plt.show()

