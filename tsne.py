import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE
import pandas as pd

path = 'csv/PC200_mainte_eval.csv'

df = pd.read_csv(path)
df = df[df.CID > 0]

data = df.loc[:,'特定自主検査':'エアコン外気フィルタ']
target = df['CID']

print(data.shape)
print(target.shape)

X_reduced = TSNE(n_components=2, random_state=0).fit_transform(data)
print(X_reduced.shape)

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=target)
for x,y,c in zip(X_reduced[:, 0], X_reduced[:, 1], target):
    plt.annotate(str(c), (x, y))

plt.colorbar()

plt.show()

'''
digits = datasets.load_digits()

print(type(digits.data))
digits_df = pd.DataFrame(digits.data)
print(digits.target)

print(digits.data.shape)
# (1797, 64)

print(digits.target.shape)
# (1797,)

X_reduced = TSNE(n_components=2, random_state=0).fit_transform(digits.data)

print(X_reduced.shape)
# (1797, 2)

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=digits.target)
for x,y,c in zip(X_reduced[:, 0], X_reduced[:, 1], digits.target):
    plt.annotate(str(c), (x, y), color='r')

plt.colorbar()

plt.show()
'''