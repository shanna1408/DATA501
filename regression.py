import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv('datasets/rank_econ.csv')
print(data.describe())

# Goal 1
G1 = data[['ar score', 'Unemployment (%)']].copy()
G1.rename(columns={"ar score": "AR"}, inplace = True)
G1.rename(columns={"Unemployment (%)": "Unemployment"}, inplace = True)
print(G1.describe())

G1_lm = ols("AR ~ Unemployment", data=G1).fit()
print(G1_lm.summary())

#Goal 2
G1 = data[['ar score', 'GDP per Capita (PPP)']].copy()
G1.rename(columns={"ar score": "AR"}, inplace = True)
G1.rename(columns={"GDP per Capita (PPP)": "GDP"}, inplace = True)
G1['GDP'] = G1['GDP'].str.replace(',', '').str.replace('$', '').astype(int)
print(G1.describe())

G1_lm = ols("AR ~ GDP", data=G1).fit()
print(G1_lm.summary())


# Goal 4 and 5
data = data.dropna()
y_train = data.pop('2019 Score');
X_train = data[['ar score', 'er score']].copy()
X_train_lm = sm.add_constant(X_train)
G2_lm = sm.OLS(y_train, X_train_lm).fit()
print(G2_lm.summary())


