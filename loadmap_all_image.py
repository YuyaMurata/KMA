import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import linecache
import sys
import os
from mpl_toolkits.mplot3d import Axes3D

path = 'C:/Users/zz17390/Documents/NetBeansProjects/KomatsuAnalyze/data/'

def heatmap(f):
    check = linecache.getline(f, int(2))
    if 'y' not in check:
        return

    df = pd.read_csv(f, engine='python', header=1)
    syaryo = linecache.getline(f, int(1))

    figure = plt.figure(figsize=(16,11))
    plt.style.use('ggplot')
    plt.rcParams["font.size"] = 14

    df_pivot = pd.pivot_table(data=df, values='v',
                                  columns='x', index='y', aggfunc=np.mean)
    #print(df_pivot)

    sns.heatmap(df_pivot, annot=True)

    plt.title(syaryo)

    #plt.show()
    plt.savefig(f+'.png')
    plt.close()

def threedbar(f):
    check = linecache.getline(f, int(2))
    if 'y' not in check:
        return

    df = pd.read_csv(f, engine='python', header=1)
    syaryo = linecache.getline(f, int(1))

    figure = plt.figure(figsize=(16, 11))
    plt.style.use('ggplot')
    plt.rcParams["font.size"] = 14
    plt.title(syaryo)

    xl = sorted(set(df['x']))
    yl = sorted(set(df['y']))

    print(xl)
    print(yl)

    dx = np.full(len(df['x']), (xl[1] - xl[0])/2.5)
    dy = np.full(len(df['y']), (yl[1] - yl[0])/2.5)
    dz = df['v']
    z = np.zeros(len(dx))

    ax = figure.add_subplot(111, projection='3d')
    ax.bar3d(df['x'], df['y'], z, dx, dy, dz)

    #plt.show()
    plt.savefig(f + '_3d.png')
    plt.close()

def bar(f):
    check = linecache.getline(f, int(2))
    if 'y' in check:
        return

    df = pd.read_csv(f, engine='python', header=1)
    syaryo = linecache.getline(f, int(1))

    figure = plt.figure(figsize=(16, 11))
    plt.style.use('ggplot')
    plt.rcParams["font.size"] = 11
    plt.title(syaryo)

    x = [str(s) for s in df['x']]
    plt.bar(x, df['v'])
    plt.title(syaryo)

    plt.ylabel("Hour")

    #plt.show()
    plt.savefig(f + '.png')
    plt.close()

def main():
    #Test
    #bar(path+'loadmap/'+'LOADMAP_可変マッチング.csv')
    #exit(0)

    for root, dirs, files in os.walk(path):
        print(root)
        print(dirs)
        print(files)

        for file in files:
            #グラフ化しないものを除外
            if 'SMR' in file or 'TIME' in file or '.png' in file:
                continue

            print(root+'/'+file)
            heatmap(root+'/'+file)
            threedbar(root + '/' + file)
            bar(root + '/' + file)

if __name__ == '__main__':
    main()