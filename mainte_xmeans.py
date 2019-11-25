import pyclustering
from pyclustering.cluster import xmeans
import numpy as np
import pylab
import pandas as pd

filename = 'file/PC200_mainte_eval.csv'

mdata = pd.read_csv(filename, index_col='SID', delimiter=',', encoding='SJIS')
mdata = mdata[mdata.AVG >= 0]
data = mdata.iloc[:,3:10] #5,13 pump
print(data)

init_center = pyclustering.cluster.xmeans.kmeans_plusplus_initializer(data.values, 2).initialize() # 初期値決定　今回は、初期クラスタ2です

xm = pyclustering.cluster.xmeans.xmeans(data.values, init_center, ccore=False)
xm.process()

clusters = xm.get_clusters()
print(len(set(clusters[0])))
print(clusters)
axdata = mdata.iloc[:,[1,10]]  #1,10 #2,3

pyclustering.utils.draw_clusters(axdata.values, clusters)