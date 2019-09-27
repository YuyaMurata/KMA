import linecache

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import os
import seaborn as sns

path = "C:/Users/zz17807/OneDrive - Komatsu Ltd/車両負荷マップ/file/"
root = os.listdir(path)

for f in root:
    csv = pd.read_csv(path+f, skiprows=1, engine='python').dropna(axis = 1, how = 'any')
    csv.T.plot.bar()
    plt.show()
    exit(0)