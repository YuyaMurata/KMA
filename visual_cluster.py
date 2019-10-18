import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

filename = 'file/PC200_mainte_eval.csv'

data = pd.read_csv(filename, index_col='SID', delimiter=',')

print(data)
n = int(max(data.CID))

xs = 'AGE'
ys = 'AVG'

cl = ['r', 'g', 'b']

for i in range(0,n+1):
    c = data[data.CID == i]
    name = 'C'+str(i)
    plt.scatter(c[xs], c[ys], c = cm.cmaps_listed.get(i), alpha=0.3, label=name)

plt.legend(loc=4)

plt.xlabel("X")
plt.ylabel("Y")


plt.show()