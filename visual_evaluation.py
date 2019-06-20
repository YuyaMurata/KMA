import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

path = 'csv/PC200_評価結果.csv'

data = pd.read_csv(path, index_col='SID', delimiter=',')

c = {}

for i in range(3):
    for j in range(3):
        key = str(i+1)+str(j+1)
        c[key] = data[(data.メンテナンスCID == i+1) & (data.使われ方CID == j+1)]

