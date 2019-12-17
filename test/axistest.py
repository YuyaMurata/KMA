import pandas as pd

path = '../out/3,0_FR.csv'
data = pd.read_csv(path, index_col=0, delimiter=',', header = 2, encoding='SJIS')
data = data[data.index <= 10000]

print(data)