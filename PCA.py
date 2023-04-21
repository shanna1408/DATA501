from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

combined_df = pd.read_csv('./datasets/rank_econ.csv')

# Basically groups scores of institutions into 2
def getCategory(x):
  if (float(x) < 75):
    return "Below 75"
  else:
    return "Above 75"
  
# Variables we use
features = ['ar score', 'er score', 'fsr score', 'cpf score', 'ifr score', 'isr score', 'irn score', 'ger score']

# Drop nan's group scores of institutions into 2
combined_df = combined_df.dropna()
combined_df['2019 Score'] = combined_df['2019 Score'].apply(lambda x: getCategory(x))

# Resets indices to 0,1,2,...
combined_df = combined_df.reset_index(drop=True)

# Standarize the values in our dataset
x = combined_df.loc[:, features].values
x = StandardScaler().fit_transform(x)

# Do the PCA stuff
pca_breast = PCA(n_components=2)
principalComponents_breast = pca_breast.fit_transform(x)
principal_breast_Df = pd.DataFrame(data = principalComponents_breast
             , columns = ['principal component 1', 'principal component 2'])
print('Explained variation per principal component: {}'.format(pca_breast.explained_variance_ratio_))
principal_breast_Df['y'] = combined_df['2019 Score']


# Create visualization
plt.figure(figsize=(10,10))
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Principal Component - 1',fontsize=15)
plt.ylabel('Principal Component - 2',fontsize=15)
plt.title("Principal Component Analysis of 2019 Economy Score",fontsize=20)
targets = ["Below 75", "Above 75"]
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = combined_df['2019 Score'] == target
    plt.scatter(principal_breast_Df.loc[indicesToKeep, 'principal component 1']
               , principal_breast_Df.loc[indicesToKeep, 'principal component 2'], c = color, s = 60)

plt.legend(targets,prop={'size': 15})

plt.show()