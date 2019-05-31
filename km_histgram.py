import pandas as pd
import matplotlib.pyplot as plt
import os
import linecache

filename = 'csv/PC200_parts_hist_graph.csv'
data = pd.read_csv(filename, index_col='データ区間', header=0)

print(data)

data.plot(kind='bar', subplots=True,layout=(6,8))
plt.show()