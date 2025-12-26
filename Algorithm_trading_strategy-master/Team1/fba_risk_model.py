import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import cvxpy as cvx

get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


price = pd.read_csv('./nav.csv')
portfolio = pd.read_csv('./portfolio_description.csv')


index = portfolio.Mid=='Emerging'
portfolio_1= portfolio[index]['Ticker'].head(5)
emerging_ticker = portfolio_1.values


final_data = price.loc[:, emerging_ticker]

returns = final_data.pct_change()[1:].fillna(0)

mean_return = returns.mean()


returns = returns - mean_return


from sklearn.decomposition import PCA

pca = PCA(n_components = returns.shape[1])

pca.fit(returns)

pca = PCA(n_components = 3)
pca.fit(returns)

factor_betas_ = pd.DataFrame(
            data=pca.components_.T,
            index=returns.columns)



factor_returns_ = pd.DataFrame(
            data=pca.transform(returns),
            index=returns.index)
factor_returns_.shape


common_returns_ = pd.DataFrame(
data=np.dot(factor_returns_, factor_betas_.T),
index= returns.index, 
columns = returns.columns)

residuals_ = (returns - common_returns_)


factor_cov_matrix_ = np.diag(
    factor_returns_.var(axis=0, ddof=1)*252
)
        
idio_var_matrix_ = pd.DataFrame(
    data=np.diag(np.var(residuals_))*252,index=returns.columns)
idio_var_vector_ = pd.DataFrame(
    data=np.diag(idio_var_matrix_.values),
    index=returns.columns
)

B = factor_betas_
F = factor_cov_matrix_
S = np.diag(idio_var_vector_.values.flatten())


def risk_function(x):
    f = np.dot(B.values.T, x)
    return np.dot(f.T, np.dot(F, f)) + np.dot(x, np.dot(S, x))

