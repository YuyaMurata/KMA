import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import linecache
import gc

path = "PC200SMR調査/"
files = os.listdir(path)

cnt = 0

print(files)
for file in files:
    name = path + file.replace('.csv', '.png')

    if name in file:
        continue

    if '.png' in file:
        continue

    fig = plt.figure(figsize=(10, 7))

    print(file)
    #dateparse = lambda x: pd.datetime.strptime(x, '%Y%m%d')
    data = pd.read_csv(open(path+file, 'r'), index_col='DATE')

    data.index = pd.to_datetime(data.index)

    print(data)

    #ax1 = data['KOMTRAX_SMR'].plot(c='black', ls='--')
    #ax2 = data['SMR'].plot(ax = ax1, c='r', ls='--')
    #ax3 = data['F_SMR'].plot(ax = ax2, alpha=0.8, c='y', lw=5)
    #data['F_KOMTRAX_SMR'].plot(ax = ax3,alpha=0.2, c='b', lw=5)

    plt.plot(data['KOMTRAX_SMR'], c='black', ls='--')
    plt.plot(data['SMR'],  c='r', ls='--')
    plt.plot(data['F_SMR'], alpha=0.8, c='y', lw=5)
    plt.plot(data['F_KOMTRAX_SMR'], alpha=0.2, c='b', lw=5)

    plt.legend(loc=4)
    #plt.show()

    name = path+file.replace('.csv', '.png')
    fig.savefig(name)

    cnt += 1
    plt.close()


    #exit(0)