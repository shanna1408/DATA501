import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

education_df = pd.read_csv('../datasets/world_rankings.csv')
economy_df = pd.read_csv('../datasets/economic_freedom.csv',encoding_errors='ignore')
combined_df = pd.read_csv('../datasets/rank_econ.csv')


""" Compare data between the institutions in the most economically successful countries in the world and unsuccessful countries in the world. """
Get top 3 and bottom 3 successful countries
economy_df = economy_df[['Country Name', 'World Rank']]
economy_df = economy_df.dropna()
sorted_df = economy_df.sort_values(by=['World Rank'])
print(sorted_df.head(3)['Country Name'])
print(sorted_df.tail(3)['Country Name'])

top_3_df = combined_df[(combined_df['Country'] == 'Hong Kong') | (combined_df['Country'] == 'Singapore') | (combined_df['Country'] == 'New Zealand')]
bottom_3_df = combined_df[(combined_df['Country'] == 'Cuba') | (combined_df['Country'] == 'Venezuela') | (combined_df['Country'] == 'Korea, North')]
top_and_bottom_3_df = economy_df[(economy_df['Country Name'] == 'Hong Kong') | (economy_df['Country Name'] == 'Singapore') | (economy_df['Country Name'] == 'New Zealand') | (economy_df['Country Name'] == 'Cuba') | (economy_df['Country Name'] == 'Venezuela') | (economy_df['Country Name'] == 'Korea, North')]


# Compare data

plt.show()