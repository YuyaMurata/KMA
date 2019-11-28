import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import os

path = 'out'

'''
args = sys.argv
#引数の処理
if len(args) <= 1:
    print("参照するファイルが見つかりません！")
    exit(0)
if len(args) > 1:
    path = args[1]
'''
fig, ax1 = plt.subplots()

root = [f for f in os.listdir(path) if 'FR.csv' in f]

for file in root:
    print(file)
    data = pd.read_csv(path+'/'+file, index_col=0, delimiter=',', encoding='SJIS')
    ax1.plot(data.index, data['COUNT'])
    ax2 = ax1.twinx()
    ax2.plot(data.index, data['RATE'])

    plt.xlim(0, 10000)
    plt.show()
    exit(0)