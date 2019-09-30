import linecache
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import os
import seaborn as sns

path = "C:/Users/zz17807/OneDrive - Komatsu Ltd/車両負荷マップ/file/"
root = os.listdir(path)

def bargraph(f, csv, fig):
    ax = fig.add_subplot(111)
    ax.set_ylabel("Hour")
    if 'ポンプ' in f:
        ax.set_xlabel("Press.")
    else:
        ax.set_xlabel("Temp.")

    csv.T.plot.bar(ax=ax, legend=None)


def d3graph(f, csv, fig):
    ax = fig.gca(projection='3d')
    ax.set_zlabel('Hour')
    if '水温' in f:
        ax.set_xlabel('Water Temp.')
        ax.set_ylabel('Oil Temp.')
    else:
        ax.set_xlabel('Torque')
        ax.set_ylabel('Engine')

    x = list(map(np.float32, [s.replace('_', '') for s in csv.columns.values]))
    y = list(map(np.float32, [s.replace('_', '') for s in csv.index.values]))

    X, Y = np.meshgrid(x, y)
    X, Y = X.ravel(), Y.ravel()
    Z = csv.as_matrix().ravel()

    l = len(Z)

    dx = 0.5*(x[1] - x[0])
    dy = 0.5*(y[1] - y[0])

    surf = ax.bar3d(X, Y, np.zeros(l), dx*np.ones(l), dy*np.ones(l), Z, edgecolor='black', shade=True)

def main():
    for f in root:
        if '.png' in f:
            continue
        plt.rcParams["font.size"] = 14
        fig = plt.figure(figsize=(16, 11))
        csv = pd.read_csv(path + f, skiprows=1, index_col=0, engine='python').dropna(axis=1, how='any')
        if 'VS' in f:
            d3graph(f, csv, fig)
        else:
            bargraph(f, csv, fig)
        plt.savefig(path+f + '.png')
        plt.close()
        #exit(0)


if __name__ == '__main__':
    main()