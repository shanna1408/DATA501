from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

combined_df = pd.read_csv('./datasets/rank_econ.csv')

# Basically groups scores of institutions into 2
def getCategory(x):
  if (x == "-" or float(x) < 50):
    return "Below 50"
  else:
    return "Above 50"

# Variables we use
features = ['GDP (Billions, PPP)', 'GDP Growth Rate (%)', '5 Year GDP Growth Rate (%)', 'GDP per Capita (PPP)', 'Unemployment (%)']

# Convert dollars into float
combined_df['GDP (Billions, PPP)'] = combined_df['GDP (Billions, PPP)'].replace('[\$,]', '', regex=True).astype(float)
combined_df['GDP per Capita (PPP)'] = combined_df['GDP per Capita (PPP)'].replace('[\$,]', '', regex=True).astype(float)

# group scores of institutions into 2
combined_df['score scaled'] = combined_df['score scaled'].apply(lambda x: getCategory(x))


# print(combined_df['score scaled'])

# Standarize the values in our dataset
df_features = combined_df.loc[:, features].values
df_features = StandardScaler().fit_transform(df_features)

# Do the PCA stuff
pca_institution_score = PCA(n_components=2)
principal_components_score_scaled = pca_institution_score.fit_transform(df_features)
pca_df = pd.DataFrame(data = principal_components_score_scaled
             , columns = ['principal component 1', 'principal component 2'])
print('Explained variation per principal component: {}'.format(pca_institution_score.explained_variance_ratio_))
pca_df['y'] = combined_df['score scaled']


# Create visualization
plt.figure(figsize=(10,10))
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Principal Component - 1',fontsize=15)
plt.ylabel('Principal Component - 2',fontsize=15)
plt.title("Principal Component Analysis of Overall University Scores",fontsize=20)
targets = ['Below 50', 'Above 50']
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = combined_df['score scaled'] == target
    plt.scatter(pca_df.loc[indicesToKeep, 'principal component 1']
               , pca_df.loc[indicesToKeep, 'principal component 2'], c = color, s = 80)

plt.legend(targets,prop={'size': 15})

plt.show()