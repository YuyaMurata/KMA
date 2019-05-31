import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

filename = 'csv/filter5y_device_smr_year_KM_PC138US_graph.csv'

data = pd.read_csv(filename, delimiter=',')
data = data[data.金額 > 0]
data = data[data.SMR > 0]
print("ALL:"+str(data.shape))

#パワーラインに絞る場合

data = data[data.パワーライン対象装置 == 1]
print('PL:'+str(data.shape[0]))

n = [str(data.shape[0]), str(data[(data.SMR<=3000) & (data.経年<=3)].shape[0]), str(data[(data.SMR<=8000) & (data.経年<=5)].shape[0])]

AD = data[data.作業形態 == 'AD']
BB = data[data.作業形態 == 'BB']
BA = data[data.作業形態 == 'BA']

#グラフ

plt.scatter(AD['経年'], AD["SMR"], s = (AD["金額"]/20000)**2, alpha=0.3, c='red', label='AD')
plt.scatter(BB['経年'], BB["SMR"], s = (BB["金額"]/20000)**2, alpha=0.3, c='green', label='BB')
plt.scatter(BA['経年'], BA["SMR"], s = (BA["金額"]/20000)**2, alpha=0.3, c='blue', label='BA')

#Annotation
plt.axhline(y=5000,  c='k', ls='--')
plt.plot([3,3], [0,5000], c='k', ls='--')
plt.plot([0,5], [8000,8000], c='k', ls='--')
plt.plot([5,5], [0,8000], c='k', ls='--')

plt.axis([0,10,0,10000])
plt.text(0+0.1,10000-100,'ALL:'+n[0],ha='left', va='top')
plt.text(0+0.1,5000-100,'N:'+n[1],ha='left', va='top')
plt.text(0+0.1,8000-100,'N:'+n[2],ha='left', va='top')

plt.legend(loc=4)

plt.xlabel("year")
plt.ylabel("smr")

plt.show()
