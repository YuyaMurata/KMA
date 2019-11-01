import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pyclustering
from pyclustering.cluster import xmeans
import pylab

filename = 'file/PC200_mainte_eval_kmpp_10_10t.csv'

data = pd.read_csv(filename, index_col='SID', delimiter=',')

print(data)
n = int(max(data.CID))

clusters = data.iloc[:,11].values
axdata = data.iloc[:,[1,10]]
print([clusters.tolist()])

#pyclustering.utils.draw_clusters(axdata.values, [clusters.tolist()])

xs = 'AGE'
ys = 'AVG'

cl =data['CID'].tolist()

for i in range(0,n+1):
    c = data[data.CID == i]
    name = 'C'+str(i)
    plt.scatter(c[xs], c[ys], c = cm.cmaps_listed.get(cl.index(i)), s=5,  label=name)

print('cluster:'+str(len(set(data['CID'].values))))

#plt.legend(loc=4)

plt.xlabel("X")
plt.ylabel("Y")


plt.show()