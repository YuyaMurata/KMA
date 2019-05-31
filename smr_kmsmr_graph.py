import pandas as pd
import matplotlib.pyplot as plt
import os
import linecache

print(os.getcwd())

#filename = 'py/csv/graph_temp.csv'
filename = 'csv/graph_temp_smr.csv'
filename2 = 'csv/graph_temp_kmsmr.csv'

#mdata = pd.read_csv(filename)
#mdata.plot(x='Date', y='SMR', marker='o', label='SMR')
#plt.legend()
#plt.show()

dateparse = lambda x: pd.datetime.strptime(x, '%Y%m%d')
data = pd.read_csv(filename, index_col='Date', header=1)
kmdata = pd.read_csv(filename2, index_col='Date', header=1)

data.index = pd.to_datetime(data.index, format='%Y%m%d')
kmdata.index = pd.to_datetime(kmdata.index, format='%Y%m%d')

alldata = pd.concat([data, kmdata], axis=1)
alldata = alldata.interpolate(method='index')

# 折れ線グラフを出力
print(data)
print(data.index)
print(kmdata)
print(kmdata.index)

print(alldata)

ax = kmdata.plot(c='black')
data.plot(ax=ax, ls='--')
#alldata.plot(y=['SMR', 'KMSMR'], linestyle='--')

#plt.plot(alldata.index, alldata['SMR'], marker='o', label='SMR')
#plt.plot(alldata.index, alldata['KMSMR'], alpha=0.5, marker='x', linestyle="--", label='KOMTRAX')
#plt.plot(data['Date'], data['REG'], alpha=1.0, c='g', linestyle="--", label='REG')
#plt.legend()
#plt.show()

#plt.fill_between(data['Date'].values, data['SMR'], data['REG'], facecolor='y',alpha=0.5)
#data.plot(x='Date', y='SGTest', alpha=1.0, linestyle="--", label='SGTest')
#plt.legend()
#plt.show()

#data = data.dropna()
#data.plot(x='Date', y='Result', alpha=1.0, marker='o', label='Result')

plt.gcf().autofmt_xdate()
syaryo = linecache.getline(filename, int(1))
print(syaryo)
plt.title(syaryo.replace('Syaryo,', ''),size=10)
plt.subplots_adjust(right=0.8)
#ncol = 2
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=8)
plt.show()
