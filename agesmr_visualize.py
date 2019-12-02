import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import codecs
import os
import linecache

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
root = [f for f in os.listdir(path) if '1,0_FR.csv' in f]

def graph(data, setting_info, analize_info):
    fig = plt.figure()
    fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.1)
    #fig.subplots_adjust(right=0.85)
    #fig.subplots_adjust(left=0.15)

    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()
    #ax3 = ax1.twinx()

    ax1.set_xlabel(setting_info.split(',')[1] + '(dx=' + setting_info.split(',')[3] + ')')

    ax1.set_ylabel('P')
    ax2.set_ylabel('Rate')
    #ax3.set_ylabel('Count')

    #rspine = ax3.spines['right']
    #rspine.set_position(('axes', 1.1))

    plt.text(0.01, 0.9, analize_info.replace(',', '\n'), horizontalalignment='left', verticalalignment='top', family='monospace',
             transform=ax1.transAxes, fontsize=18)
    plt.xlim(0, 10000)

    ax1.plot(data.index, data['COUNT'], label='Population')
    ax2.plot(data.index, data['RATE'], c='red', label='Failure Rate')
    #ax3.bar(data.index, data['FAIL'], label='Failure Count')

    #h1, l1 = ax1.get_legend_handles_labels()
    #h2, l2 = ax2.get_legend_handles_labels()
    #h3, l3 = ax3.get_legend_handles_labels()
    #ax1.legend(h1 + h2 + h3, l1 + l2 + l3)
    #ax1.legend(h1 + h2, l1 + l2)

    plt.xticks(color="None")
    plt.yticks(color="None")

    plt.show()

    #plt.savefig(file.replace('.csv', '.png'))

    plt.close()

for f in root:
    file = path+'/'+f
    data = pd.read_csv(file, index_col=0, delimiter=',', header = 2, encoding='SJIS')

    lines = codecs.open(file, encoding='SJIS').readlines()
    setting_info = lines[0].strip()
    analize_info = lines[1].strip()

    print(setting_info)
    print(analize_info)
    print(data)

    graph(data, setting_info, analize_info)