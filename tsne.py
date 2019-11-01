import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE
import pandas as pd
from sklearn import preprocessing, decomposition

path = 'file/PC200_mainte_eval_kmpp_10_10t.csv'

df = pd.read_csv(path)
df = df[df.CID > 0]

data = df.iloc[:, 4:11]
target = df['CID']

print(data)

def tsne():

    print(data.shape)
    print(target.shape)

    X_reduced = TSNE(n_components=2, random_state=0).fit_transform(data)
    print(X_reduced.shape)

    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=target)
    # for x,y,c in zip(X_reduced[:, 0], X_reduced[:, 1], target):
    #    plt.annotate(str(c), (x, y), size=5)

    plt.colorbar()

    plt.show()

def pca():
    pca = decomposition.PCA(n_components=2)
    X_transformed = pca.fit_transform(data)

    print(X_transformed.shape)

    # 解説5: 主成分分析の結果-----------------------------
    print("主成分の分散説明率")
    print(pca.explained_variance_ratio_)
    print("固有ベクトル")
    print(pca.components_)

    plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=target)

    plt.show()

if __name__ == '__main__':
    pca()
    #tsne()