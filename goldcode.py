# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:24:19 2020

@author: Maboko Seabi
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gold.csv')
df['Date'] = pd.to_datetime(df['Date'])
#df = df.set_index('Date')

pd.set_option('display.max_columns',14)

#The previous close is shifted up to the day before
df['Price1'] = df['Close'].shift(-1)

#Price1 was moved up so that we can get the difference in price
df['PriceDiff'] = df['Price1'] - df['Close'] 

df['Return'] = df['PriceDiff']/df['Close']

#calculating eimple moving average 
df['MA50'] = df['Close'].rolling(50).mean()
df['MA200'] = df['Close'].rolling(200).mean()

fig,(ax1,ax2) = plt.subplots(nrows=2,ncols=1,sharex=True)

ax1.plot(df['Date'],df['MA50'],color='g',label='MA50')
ax1.plot(df['Date'],df['MA200'],color='r',label='MA200')
ax1.plot(df['Date'],df['Close'],label='Close Price')
ax2.plot(df['Date'],df['Return'])

ax1.set_title('Gold price between 2015/03/18-2020/03/17')
ax1.set_ylabel('Price of Gold $')
ax1.legend()
ax1.grid()

ax2.set_title('Return on Gold')
ax2.set_ylabel('Return Ratio')

ax2.grid()

plt.tight_layout()
plt.show()
