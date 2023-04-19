import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../datasets/world_rankings.csv')

""" Understand which countries have the universities with the highest and lowest quality of education. """
df2 = df[["location", "score scaled"]]
df2['score scaled'] = pd.to_numeric(df2['score scaled'], errors='coerce')
df2 = df2.dropna()
df2 = df2.groupby(["location"]).mean()
df2['location'] = df2.index
df2 = df2.sort_values(by=['score scaled'])
print(df2)
lowest_5_df = df[(df['location'] == 'Turkey') | (df['location'] == 'Cyprus') | (df['location'] == 'Uruguay') | (df['location'] == 'Cuba') | (df['location'] == 'Greece')]
lowest_5_df['score scaled'] = pd.to_numeric(lowest_5_df['score scaled'], errors='coerce')
lowest_5_vis = sns.boxplot(data=lowest_5_df, x="score scaled", y="location", showmeans=True, order=["Turkey", "Cyprus", "Uruguay", "Cuba", "Greece"])
lowest_5_vis.set_title('Top 5 countries with lowest overall score')


plt.show()