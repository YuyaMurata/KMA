import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

#filename = 'csv/test_cluster_km.csv'
#filename = 'csv/test_cluster_kmp.csv'
#filename = 'csv/PC200_evaluation.csv'
filename = 'csv/PC200_mainte_eval.csv_attched_lcc.csv'

data = pd.read_csv(filename, index_col='SID', delimiter=',')

print(data)

c0 = data[data.CID == 0]
c1 = data[data.CID == 1]
c2_1 = data[data.CID == 2]
c2_2 = data[data.CID == 3]
c2_3 = data[data.CID == 4]
c3 = data[data.CID == 5]

xs = 'y'
ys = 'AVG'

cl = ['r', 'g', 'lightblue', 'steelblue', 'dodgerblue', 'y']

#plt.scatter(rdata[xs], rdata[ys], c='black', alpha=0.5, label='RENT')

plt.scatter(c0[xs], c0[ys], c=cl[0], alpha=0.3, label='C0')
plt.scatter(c1[xs], c1[ys], c=cl[1], alpha=0.3, label='C1')
plt.scatter(c2_1[xs], c2_1[ys], c=cl[2], alpha=0.5, label='C2_1')
plt.scatter(c2_2[xs], c2_2[ys], c=cl[3], alpha=0.5, label='C2_2')
plt.scatter(c2_3[xs], c2_3[ys], c=cl[4], alpha=0.5, label='C2_3')
plt.scatter(c3[xs], c3[ys], c=cl[5], alpha=0.3, label='C3')



#cid = data[t1:t1].CID
#plt.text(data[t1:t1][xs], data[t1:t1][ys],t1,ha='left', va='top')
#plt.scatter(data[t1:t1][xs], data[t1:t1][ys], c= cl[int(cid)], s=100)
#cid = data[t2:t2].CID
#plt.text(data[t2:t2][xs], data[t2:t2][ys],t2,ha='left', va='top')
#plt.scatter(data[t2:t2][xs], data[t2:t2][ys], c= cl[int(cid)], s=100)

plt.legend(loc=4)

plt.xlabel("X")
plt.ylabel("Y")


plt.show()