#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore


price = pd.read_csv('./nav.csv')
portfolio = pd.read_csv('./portfolio_description.csv')


index = portfolio.Mid == 'Emerging'
portfolio_1 = portfolio[index]['Ticker'].head(5)
emerging_ticker = portfolio_1.values


final_data = pd.concat([price.loc[:,'Date'],price.loc[:,emerging_ticker]], axis =1)


ticker_names = ['EWZ', '105010', 'DGS', 'ILF', 'EPI']


window_length = 252

t1 = np.arange(1, window_length+1)
t2 = np.arange(1, window_length+1)**2
X = np.array([t1, t2]).T



beta = {'Date': [], 'EWZ': [], '105010': [], 'DGS': [], 'ILF': [], 'EPI': []}
gamma = {'Date': [], 'EWZ': [], '105010': [], 'DGS': [], 'ILF': [], 'EPI': []}

for day in range(len(final_data)):
        if day > 252:  
            beta['Date'].append(final_data.loc[day,'Date'])
            gamma['Date'].append(final_data.loc[day,'Date'])

for name in ticker_names:
    for day in range(len(final_data)):
        if day > 252:                   
            y = final_data.loc[day-window_length+1:day, name]

            if np.all(np.isfinite(y)):
                regressor = LinearRegression()
                regressor.fit(X,y)

                beta[name].append(regressor.coef_[0])
                gamma[name].append(regressor.coef_[1])

            else:
                beta[name].append(np.nan)
                gamma[name].append(np.nan)


beta_df = pd.DataFrame(beta).set_index('Date')
beta_df = beta_df.rank(axis = 1)
beta_df = beta_df.rename(index={})



gamma_df = pd.DataFrame(gamma).set_index('Date')
gamma_df = gamma_df.rank(axis =1)



conditional_factor_emerging = (beta_df * gamma_df).rank(axis = 1).apply(zscore, axis='columns').T



index = portfolio.Mid == 'Metal'
portfolio_1 = portfolio[index]['Ticker']
metal_ticker = portfolio_1.values



final_data = pd.concat([price.loc[:,'Date'],price.loc[:,metal_ticker]], axis =1)


ticker_names = ['GLD', 'SLV', 'PPLT', 'PALL', '9081', 'DBB', 'ALUM']


window_length = 252

t1 = np.arange(1, window_length+1)
t2 = np.arange(1, window_length+1)**2
X = np.array([t1, t2]).T



beta = {'Date': [], 'GLD': [], 'SLV': [], 'PPLT': [], 'PALL':[], '9081':[], 'DBB':[], 'ALUM':[]}
gamma = {'Date': [], 'GLD': [], 'SLV': [], 'PPLT': [], 'PALL':[], '9081':[], 'DBB':[], 'ALUM':[]}

for day in range(len(final_data)):
        if day > 252:  
            beta['Date'].append(final_data.loc[day,'Date'])
            gamma['Date'].append(final_data.loc[day,'Date'])

for name in ticker_names:
    for day in range(len(final_data)):
        if day > 252:                   
            y = final_data.loc[day-window_length+1:day, name]

            if np.all(np.isfinite(y)):
                regressor = LinearRegression()
                regressor.fit(X,y)

                beta[name].append(regressor.coef_[0])
                gamma[name].append(regressor.coef_[1])

            else:
                beta[name].append(np.nan)
                gamma[name].append(np.nan)


beta_df = pd.DataFrame(beta).set_index('Date')
beta_df = beta_df.rank(axis = 1)
beta_df = beta_df.rename(index={})



gamma_df = pd.DataFrame(gamma).set_index('Date')
gamma_df = gamma_df.rank(axis =1)


conditional_factor_metal = (beta_df * gamma_df).rank(axis = 1).apply(zscore, axis='columns').T


