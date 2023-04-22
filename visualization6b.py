import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

education_df = pd.read_csv('datasets/world_rankings.csv')
economy_df = pd.read_csv('datasets/economic_freedom.csv',encoding_errors='ignore')
combined_df = pd.read_csv('datasets/rank_econ.csv')

top_3_df = combined_df[(combined_df['Country'] == 'Hong Kong') | (combined_df['Country'] == 'Singapore') | (combined_df['Country'] == 'New Zealand')]
bottom_3_df = combined_df[(combined_df['Country'] == 'Cuba') | (combined_df['Country'] == 'Venezuela') | (combined_df['Country'] == 'Korea, North')]
