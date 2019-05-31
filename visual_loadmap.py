import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df_flights = pd.read_csv("csv/loadmap_part1.csv")#sns.load_dataset('flights')

df_flights_pivot = pd.pivot_table(data=df_flights, values='v',
                                  columns='x', index='y', aggfunc=np.mean)
print(df_flights_pivot)

sns.heatmap(df_flights_pivot, annot=True)


plt.show()