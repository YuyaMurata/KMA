import pandas as pd
import matplotlib.pyplot as plt
from sksurv.nonparametric import kaplan_meier_estimator

path = 'csv/PC200_agesmr_eval.csv'

data = pd.read_csv(path, index_col='SID', delimiter=',')

c = {}

for i in range(3):
    for j in range(3):
        key = str(i+1)+str(j+1)
        c[key] = data[(data.メンテナンスCID == i+1) & (data.使われ方CID == j+1)]

        figure = plt.figure()

        time, survival_prob = kaplan_meier_estimator(list(map(lambda i : i==1, c[key]["FSTAT"])), c[key]["SMR"])
        print(key+str(survival_prob))
        plt.step(time, survival_prob, where="post")

        plt.savefig(key+'.png')