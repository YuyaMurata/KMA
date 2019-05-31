import pandas as pd
import matplotlib.pyplot as plt

def plot_outlier(ts, ewm_span=5, threshold=2.0):
    assert type(ts) == pd.Series
    fig, ax = plt.subplots()

    ewm_mean = ts.ewm(span=ewm_span).mean()  # 指数加重移動平均
    ewm_std = ts.ewm(span=ewm_span).std()  # 指数加重移動標準偏差
    ax.plot(ts, label='original')
    ax.plot(ewm_mean, label='ewma')

    # 標準偏差から 3.0 倍以上外れているデータを外れ値としてプロットする
    ax.fill_between(ts.index,
                    ewm_mean - ewm_std * threshold,
                    ewm_mean + ewm_std * threshold,
                    alpha=0.2)
    outlier = ts[(ts - ewm_mean).abs() > ewm_std * threshold]
    ax.scatter(outlier.index, outlier, label='outlier')

    ax.legend()

    return fig

def plot_outlier2(ts, ewm_span=5, threshold=2.0):
    assert type(ts) == pd.Series
    fig, ax = plt.subplots()

    ewm_mean = ts.rolling(window=3, min_periods=3).mean()  # 指数加重移動平均
    ax.plot(ts, label='original')
    ax.plot(ewm_mean, label='ewma')

    ax.legend()

    return fig

#data = pd.read_csv('csv/350076_smr.csv', index_col='date', header=0)
data = pd.read_csv('csv/452771_smr.csv', index_col='date', header=0)

data.index = pd.to_datetime(data.index, format='%Y%m%d')
df = data.asfreq('D')

df_in = df.interpolate()
print(df_in)

#df_in.plot()

plot_outlier2(df.dropna()['smr'])

#df_in.plot()
plt.show()