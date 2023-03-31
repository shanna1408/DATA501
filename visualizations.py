import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('datasets/world_rankings.csv')
combined_df = pd.read_csv('datasets/rank_econ.csv')

""" Understand the connection between academic reputation and employability. """
# plot1 = sns.regplot(x="ar score", y="er score", data=df)
# plot1.set(xlabel='Academic Reputation Score', ylabel='Employer Reputation Score')
# plot1.set_title('Academic Reputation Score vs Employer Reputation Score')


""" Understand which countries have the universities with the highest and lowest quality of education. """
# df2 = df[["location", "score scaled"]]
# df2['score scaled'] = pd.to_numeric(df2['score scaled'], errors='coerce')
# df2 = df2.dropna()
# df2 = df2.groupby(["location"]).mean()
# df2['location'] = df2.index
# df2 = df2.sort_values(by=['score scaled'])
# print(df2)
# top_5_df = df[(df['location'] == 'Singapore') | (df['location'] == 'Switzerland') | (df['location'] == 'United Kingdom') | (df['location'] == 'Hong Kong SAR') | (df['location'] == 'United States')]
# top_5_df['score scaled'] = pd.to_numeric(top_5_df['score scaled'], errors='coerce')
# top_5_vis = sns.boxplot(data=top_5_df, x="score scaled", y="location", showmeans=True, order=["United States", "United Kingdom", "Switzerland", "Hong Kong SAR", "Singapore"])
# top_5_vis.set_title('Top 5 countries with highest overall score')
# lowest_5_df = df[(df['location'] == 'Turkey') | (df['location'] == 'Cyprus') | (df['location'] == 'Uruguay') | (df['location'] == 'Cuba') | (df['location'] == 'Greece')]
# lowest_5_df['score scaled'] = pd.to_numeric(lowest_5_df['score scaled'], errors='coerce')
# lowest_5_vis = sns.boxplot(data=lowest_5_df, x="score scaled", y="location", showmeans=True, order=["Turkey", "Cyprus", "Uruguay", "Cuba", "Greece"])
# lowest_5_vis.set_title('Top 5 countries with lowest overall score')


""" Understand whether academic quality actually has an effect on employability. """
# df3 = combined_df[["Country", "score scaled", "Unemployment (%)"]]
# df3['score scaled'] = pd.to_numeric(df3['score scaled'], errors='coerce')
# df3 = df3.dropna()
# df3 = df3.groupby(["Country"]).mean()
# print(df3)
# plot3 = sns.regplot(x="score scaled", y="Unemployment (%)", data=df3)
# plot3.set(xlabel='score scaled', ylabel='Unemployment (%)')
# plot3.set_title('Academic quality vs Unemployment')


""" Understand the connection between economic success of a country and quality of education. """



""" Understand the connection between economic success of a country and employability of institutions. """




""" Compare data between the institutions in the most economically successful countries in the world and unsuccessful countries in the world. """




""" Compare data between various countries and Canada. """




plt.show()
