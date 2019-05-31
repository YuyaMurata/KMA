import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA

print(os.getcwd())

filename = 'csv/graph_temp.csv'
dateparse = lambda x: pd.datetime.strptime(x, '%Y%m%d')
#data = pd.read_csv(filename, index_col='Date',parse_dates=['Date'], date_parser=dateparse, header=1)
data = pd.read_csv(filename, index_col='Date', header=1)
data = data.dropna()
data = data.groupby(level=0).last()

smr = pd.Series(data['SMR'])
smr.index = pd.to_datetime(data.index)

difsmr = smr.diff().dropna()

print(len(smr))

#n = 491
#y = signal.savgol_filter(data, 123, 5)

#difsmr.plot()
#plt.plot(y)

# 差分系列への自動ARMA推定関数の実行
#resDiff = sm.tsa.arma_order_select_ic(difsmr, ic='aic', trend='nc')
#print(resDiff)

smr13 = smr[0:360]
print(smr13)
#ARIMA_0_1_2 = ARIMA(smr, order=(0, 1, 2)).fit(dist=False)

SARIMA_0_1_2_111 = sm.tsa.SARIMAX(smr13, order=(0,1,2), seasonal_order=(1,1,1,1)).fit()

'''
resid = ARIMA_0_1_2.resid
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
'''

'''#自己・偏自己相関
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(smr, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(smr, lags=40, ax=ax2)
'''

pred = SARIMA_0_1_2_111.forecast(60)

print(pred)
plt.plot(smr+pred)
#plt.plot(pred, "r")

plt.show()