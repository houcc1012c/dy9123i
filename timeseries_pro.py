import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as ll
from statsmodels.tsa.arima_process import arma_generate_sample
import pandas as pd
df=pd.read_csv(r'C:\Users\dy912\Desktop\HKtemperature.csv',index_col=0)
data=df.stack()
data=data-np.mean(data)
"""we first plot the data to see whether it is staionary"""
plt.plot(data.values)
"""Then,we compute the sample ACF,we see that it is not staionary"""
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(data.values, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(data.values, lags=40, ax=ax2)
"""we then take seasonal difference to see whether it is good"""
sdiff=data-data.shift(12)
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(sdiff.dropna().values, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(sdiff.dropna().values, lags=40, ax=ax2)

arma_mod30 = sm.tsa.statespace.SARIMAX(data.values, order=(0,0,0), seasonal_order=(0,1,1,12)).fit(disp=False)
resid = arma_mod30.resid
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
print(arma_mod30.summary())
"""we then try a different model"""

arma_mod30 = sm.tsa.statespace.SARIMAX(data.values, order=(1,0,0), seasonal_order=(0,1,1,12)).fit(disp=False)
resid = arma_mod30.resid
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

print(arma_mod30.summary())

"""finnaly, we tried to predict the temperature of 2018"""
m=np.mean(df.stack())
predict=m+arma_mod30.forecast(12)
print(predict)

